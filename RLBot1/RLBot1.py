import discord
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

'''
Epic: /epic/<username>
Steam: /steam/<steamId>
PS: /psn/<username>
XBox: /xbl/<username>
'''

client = discord.Client()
service = Service("C:\\Users\\simon.manzler\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--start-maximized")
#options.add_argument("--headless=new")
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

def get_info(platform, ID):
    playlistData = {}
    response = driver.get(f'{URL}/{platform}/{ID}') # going to return NoneType
    html = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/pre"))).get_attribute("innerHTML")
    data = json.loads(html)
    # error handling
    if list(data.keys())[0] == "errors":
        return("Error in returning rank")
    # playlistCount gets iterated by 1 then condition is >= 1 so it ignores lifetime
    # condition for 1 is for unranked
    # anything else is ranked playlists
    playlistCount = 0

    for data in data["data"]["segments"]:
        if playlistCount == 1:
            unrankedName = data["metadata"]["name"]  # Gives playlist name -> Unranked
            unrankedMMR = data["stats"]["rating"]["value"]
            playlistData[unrankedName] = unrankedMMR
        elif playlistCount > 1:
            currentRankedPlaylist = []
            playlistName = get_playlist(data)
            rankName = get_rank(data)
            divisionName = get_division(data)
            MMR = get_mmr(data)
            currentRankedPlaylist.append(rankName)
            currentRankedPlaylist.append(divisionName)
            currentRankedPlaylist.append(MMR)
            playlistData[playlistName] = currentRankedPlaylist
        playlistCount += 1
    return playlistData

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('-rank'):
        words = message.content.split()
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
        await message.channel.send(playlistData)  #this line sends message back to channel in discord

client.run('ODQ2Nzk2NjA1NDEwOTAyMDY3.YK0uyw.nwUPfqchJNkuAJgdHZjef_9eItA')