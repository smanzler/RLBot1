from shlex import join
import discord
import os
import PIL
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
    
def rank_number(rank):
    if rank == "Supersonic Legend":
        return 230
    elif rank == "Grand Champion III":
        return 220
    elif rank == "Grand Champion II":
        return 210
    elif rank == "Grand Champion I":
        return 200
    elif rank == "Champion III":
        return 190
    elif rank == "Champion II":
        return 180
    elif rank == "Champion I":
        return 170
    elif rank == "Diamond III":
        return 160
    elif rank == "Diamond II":
        return 150
    elif rank == "Diamond I":
        return 140
    elif rank == "Platinum III":
        return 13
    elif rank == "Platinum II":
        return 120
    elif rank == "Platinum I":
        return 110
    elif rank == "Gold III":
        return 100
    elif rank == "Gold II":
        return 90
    elif rank == "Gold I":
        return 80
    elif rank == "Silver III":
        return 70
    elif rank == "Silver II":
        return 60
    elif rank == "Silver I":
        return 50
    elif rank == "Bronze III":
        return 40
    elif rank == "Bronze II":
        return 30
    elif rank == "Bronze I":
        return 20
    elif rank == "Unranked":
        return 10
    else:
        return 0
    
def rank_num_with_division(rank, division):
    new_rank_num = rank_number(rank)
    if division == "Division I":
        return new_rank_num+1
    elif division == "Division II":
        return new_rank_num+2
    elif division == "Division III":
        return new_rank_num+3
    else:
        return new_rank_num
    
def get_highest_rank(data):
    highest_rank = 0
    for each in data["data"]["segments"][1:9]:
        num = rank_num_with_division(rank=get_rank(each), division=get_division(each))
        if (highest_rank < num):
            highest_rank = num
    return highest_rank

def get_location(ID):
    if ID == 0:
        return 100, 10
    elif ID == 1:
        return 200, 10
    elif ID == 2:
        return 300, 10
    elif ID == 3:
        return 300, 320
    elif ID == 4:
        return 300, 630
    elif ID == 5:
        return 400, 10
    elif ID == 6:
        return 400, 320
    elif ID == 7:
        return 400, 630
    elif ID == 8:
        return 500, 10
    else:
        return 0,0
    
def make_background():
    return Image.new(mode="RGB", size=(960, 540),color=(58,59,60))

def get_stats_location(ID):
    if ID == 0:
        return 100, 0, "ls"
    elif ID == 1:
        return 250, 0, "ls"
    elif ID == 2:
        return 400, 0, "ls"
    elif ID == 3:
        return 100, 450, "ms"
    elif ID == 4:
        return 250, 450, "ms"
    elif ID == 5:
        return 400, 450, "ms"
    elif ID == 6:
        return 100, 900, "rs"
    elif ID == 7:
        return 250, 900, "rs"
    elif ID == 8:
        return 400, 900, "rs"
    else:
        return 400, 10, "ls"
    
def percentageCheck(val):
    if val >= 50:
        return "Top " + str(round(100-val, 1))
    else:
        return "Bottom " + str(round(val, 1))

def get_pic(platform, ID):
    #data = get_api(platform=platform, ID=ID)
    data = getjson()
    im = Image.new(mode="RGB", size=(960, 540),color=(58,59,60)) #creates the base

    I1 = ImageDraw.Draw(im) # allows text to be added

    myFont = ImageFont.truetype('Roboto-Black.ttf', 19) #different font sizes
    myFont2 = ImageFont.truetype('Roboto-Black.ttf', 25)
    myFont3 = ImageFont.truetype('Roboto-Black.ttf', 15)

    myFont5 = ImageFont.truetype('Roboto-Black.ttf', 40)
    myFont6 = ImageFont.truetype('Roboto-Black.ttf', 30)

    myFont8 = ImageFont.truetype('Roboto-Black.ttf', 50)
    
    down_count = 10 #x value the loop starts creating pics
    across_count = 10
    count = 0

    highest_rank = get_highest_rank(data)
    first = 1

    I1.text((30, 30), (data["data"]["platformInfo"]["platformSlug"]).capitalize(), font=myFont, fill = (255, 255, 255)) #adds text
    I1.text((30, 45), data["data"]["platformInfo"]["platformUserHandle"], font=myFont8, fill = (255, 255, 255))
    
    for data in data["data"]["segments"][1:11]:
        rank = get_rank(data)
        division = get_division(data)
        if rank_num_with_division(rank, division) == highest_rank and first == 1: #checks if its the highest rank
            im2 = Image.open(r"icons\{}.webp".format(rank)).convert("RGBA") #gets icon
            im2 = im2.resize((240,240), PIL.Image.LANCZOS)
            im.paste(im2, (300, 80), mask = im2) #adds icon
            I1.text((520, 140), "Highest Rank:", font=myFont3, fill = (255, 255, 255)) #adds text
            I1.text((520, 155), get_playlist(data), font=myFont6, fill = (255, 255, 255))
            I1.text((520, 180), str(get_mmr(data)), font=myFont5, fill = (213, 182, 10))
            I1.text((520, 220), rank + " " + division, font=myFont, fill = (255, 255, 255))
            first = 0
        else:
            down_count, across_count = get_location(count) #changes location based on iteration

            im2 = Image.open(r"icons\{}.webp".format(rank)).convert("RGBA") #gets icon
            im2 = im2.resize((100,100), PIL.Image.LANCZOS)
            im.paste(im2, (across_count, down_count), mask = im2) #adds icon
            I1.text((across_count+100, down_count+25), get_playlist(data), font=myFont, fill = (255, 255, 255)) #adds text
            I1.text((across_count+100, down_count+42), str(get_mmr(data)), font=myFont2, fill = (213, 182, 10))
            I1.text((across_count+100, down_count+67), rank + " " + division, font=myFont3, fill = (255, 255, 255))
            count+=1

    im.show() #shows the image (optional)
    return im

def get_stats_pic(platform, ID):
    #data = get_api(platform=platform, ID=ID)
    data = getjson()
    platform = data["data"]["platformInfo"]["platformSlug"]
    ID = data["data"]["platformInfo"]["platformUserHandle"]
    season = data["data"]["availableSegments"][-1]["metadata"]["name"]

    data = data["data"]["segments"][0]["stats"]
    
    im = make_background() #creates the base
    
    I1 = ImageDraw.Draw(im)
    
    myFont = ImageFont.truetype('Roboto-Black.ttf', 19) #different font sizes
    myFont2 = ImageFont.truetype('Roboto-Black.ttf', 25)
    myFont3 = ImageFont.truetype('Roboto-Black.ttf', 15)
    
    myFont8 = ImageFont.truetype('Roboto-Black.ttf', 50)
    
    I1.text((30, 30), platform.capitalize(), font=myFont, fill = (255, 255, 255)) #adds text
    I1.text((30, 45), ID, font=myFont8, fill = (255, 255, 255))
    
    count = 0
    for each in data:
        if each == "seasonRewardLevel":
            I1.text((840, 30), season, font=myFont, anchor="ra", fill = (255, 255, 255))
            I1.text((840, 50), "Reward Level", font=myFont2, anchor="ra", fill = (255, 255, 255))
            im2 = Image.open(r"icons\{}.webp".format(data[each]["metadata"]["rankName"])).convert("RGBA") #gets icon
            im2 = im2.resize((100,100), PIL.Image.LANCZOS)
            im.paste(im2, (850, 15), mask = im2)
        elif each == "seasonRewardWins":
            print(percentageCheck(data['seasonRewardLevel']['percentile']))
            I1.text((840, 78), f"{percentageCheck(data['seasonRewardLevel']['percentile'])}% - {data[each]['value']} Wins", font=myFont3, anchor="ra", fill = (213, 182, 10))
        else:
            down_count, across_count, alignVal = get_stats_location(count)
            I1.text((across_count+30, down_count+30), data[each]["displayName"], font=myFont3, anchor=alignVal, fill = (255, 255, 255))
            I1.text((across_count+30, down_count+75), str(data[each]["displayValue"]), font=myFont8, anchor=alignVal, fill = (255, 255, 255))
            I1.text((across_count+30, down_count+100), f"{percentageCheck(data[each]['percentile'])}% - #{data[each]['rank']}", font=myFont3, anchor=alignVal, fill = (213, 182, 10))
            print(each)
            count+=1
        
    

    #im.show() #shows the image (optional)
    return im


def get_info(platform, ID):
    #data = get_api(platform=platform, ID=ID)
    data = getjson()
    
    # error handling
    if list(data.keys())[0] == "errors":
        return("Error in returning rank")
    
    playlistData = ""
    
    # returns iterations 1-8 of the segments
    for data in data["data"]["segments"][1:9]:
        playlistData +="{}: ({}) {} {}\n".format(get_playlist(data), get_mmr(data), get_rank(data), get_division(data))
    return playlistData.format()

def get_stats_info():
    return ""

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
        # epic == Epic
        ID = words[2]
        playlistData = get_info(platform, ID)
        print(playlistData)
        
        #await message.channel.send(playlistData)  #this line sends message back to channel in discord
        
        with BytesIO() as image_binary:# this block sends the pic (not sure how it works)
            get_pic(platform, ID).save(image_binary, 'PNG')
            image_binary.seek(0)
            await message.channel.send(file=discord.File(fp=image_binary, filename='image.png'))
    if msg.startswith('-stats'):
        words = msg.split()
        platform = words[1].lower()
        if platform == "xbox":
            platform = "xbl"
        if platform == "playstation":
            platform = "psn"
        ID = words[2]
        
        playlistData = get_stats_info(platform, ID)

client.run('ODQ2Nzk2NjA1NDEwOTAyMDY3.YK0uyw.nwUPfqchJNkuAJgdHZjef_9eItA')