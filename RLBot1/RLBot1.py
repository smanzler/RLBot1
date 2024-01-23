from shlex import join
import discord
import os
from io import BytesIO
import json
from dictparse import getjson
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

'''
Epic: /epic/<username>
Steam: /steam/<steamId>
PS: /psn/<username>
XBox: /xbl/<username>
'''

client = discord.Client()
service = Service(Path(__file__).with_name("chromedriver.exe"))
options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--start-maximized")
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)
soup = BeautifulSoup()
URL = 'https://api.tracker.gg/api/v2/rocket-league/standard/profile'

def get_playlist(data):
    return data["metadata"]["name"]  # Gives playlist name -> All ranked playlists

def get_rank(data):
    return data["stats"]["tier"]["metadata"]["name"]  # Gives rank name

def get_division(data):
    return data["stats"]["division"]["metadata"]["name"]  # Gives division name

def get_mmr(data):
    return data["stats"]["rating"]["value"]  # Gives MMR value

def get_api(platform, ID):
    response = driver.get(f'{URL}/{platform}/{ID}') # going to return NoneType
    try:
        html = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/pre"))).get_attribute("innerHTML")
        return json.loads(html)
    except:
        return getjson()    

def get_pic():
    # data = get_api(platform=platform, ID=ID)
    data = getjson()
    im = Image.new(mode="RGB", size=(300, 900),color=(58,59,60)) #creates the base

    I1 = ImageDraw.Draw(im) # allows text to be added
 
    myFont = ImageFont.truetype('Roboto-Black.ttf', 11) #different font sizes
    myFont2 = ImageFont.truetype('Roboto-Black.ttf', 17)
    myFont3 = ImageFont.truetype('Roboto-Black.ttf', 8)
    
    count = 10 #x value the loop starts creating pics
    
    for data in data["data"]["segments"][1:9]:
        im2 = Image.open(r"icons\{}.webp".format(get_rank(data))) #gets icon
        im2 = im2.resize((100,100))
        im.paste(im2, (10, count), mask = im2) #adds icon
        I1.text((120, count+30), get_playlist(data), font=myFont, fill = (255, 255, 255),) #adds text
        I1.text((120, count+40), str(get_mmr(data)), font=myFont2, fill = (139, 128, 0),)
        I1.text((120, count+57), get_rank(data) + " " + get_division(data), font=myFont3, fill = (255, 255, 255),)
        count+=110 #moves down

    im.show() #shows the image (optional)
    return im

def get_info(platform, ID):
    # data = get_api(platform=platform, ID=ID)
    data = getjson()
    
    # error handling
    if list(data.keys())[0] == "errors":
        return("Error in returning rank")
    
    playlistData = ""
    
    # returns iterations 1-8 of the segments
    for data in data["data"]["segments"][1:9]:
        playlistData +="{}: ({}) {} {}\n".format(get_playlist(data), get_mmr(data), get_rank(data), get_division(data))
    return playlistData.format()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('-rank'):
        words = msg.split()
        platform = words[1].lower()
        if platform == "xbox":
            platform = "xbl"
        if platform == "playstation":
            platform = "psn"
        # steam == Steam      just so i know the keyword for them
        # epic == Epicf
        ID = words[2]
        playlistData = get_info(platform, ID)
        print(playlistData)
        await message.channel.send(playlistData)  #this line sends message back to channel in discord
        # this block sends the pic (not sure how it works)
        with BytesIO() as image_binary:
            get_pic().save(image_binary, 'PNG')
            image_binary.seek(0)
            await message.channel.send(file=discord.File(fp=image_binary, filename='image.png'))

client.run('ODQ2Nzk2NjA1NDEwOTAyMDY3.YK0uyw.nwUPfqchJNkuAJgdHZjef_9eItA')