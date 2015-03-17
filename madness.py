import requests
from bs4 import BeautifulSoup
import time
import random

MW=["Kentucky","Kansas","Notre Dame",
    "Maryland","West Virginia",
    "Butler","Wichita","Cincinnati",
    "Purdue","Indiana","Texas",
    "Buffalo","Valparaiso","Northeastern",
    "New Mexico","playin-mw"]

E=["Villanova","Virginia","Oklahoma",
    "Louisville","Iowa","Providence",
    "Michigan State","LSU","UGA",
    "playin-e","Wyoming","Irvine",
    "Alabama","Belmont","Lafayette"]

W=["Wisconsin","Arizona","Baylor",
    "UNC","Arkansas","Xavier",
    "VCU","Oregon","Oklahoma State",
    "Ohio","playin-w",
    "Wofford","Harvard","Georgia State",
    "Texas Southern","Costal Carolina"]

S=["Duke","Gonzaga","Iowa State","Georgetown",
    "Utah","Methodist","Iowa",
    "San Diego","St John","Davidson",
    "UCLA","Austin","washington",
    "UAB","North Dakota","playin-s"]


base_url = "https://www.google.com/search?&q=%22march+madness+2015%22+"

playins = {"playin-w":["BYU","Ole Miss"],
            "playin-s":["Hampton","Manhattan"],
            "playin-e":["Boise","Dayton"],
            "playin-mw":["New Hampshire","NJIT"]}

mention_count = {}
for team in W+S+E+MW:
    if team in playins:
        team1 = playins[team][0]
        team2 = playins[team][1]
    
        r = requests.get(base_url+"%22"+team1+"%22")
        soup = BeautifulSoup(r.text)
        d = soup.find("div", {"id": "resultStats"})
        count1 = int(d.text.replace("About","").replace("results","").replace(",","").strip())
        
        r = requests.get(base_url+"%22"+team2+"%22")
        soup = BeautifulSoup(r.text)
        d = soup.find("div", {"id": "resultStats"})
        count2 = int(d.text.replace("About","").replace("results","").replace(",","").strip())
        
        mention_count[team] = (count1+count2)/2.0

        #deal with averages
    else:
        r = requests.get(base_url+"%22"+team+"%22")
        soup = BeautifulSoup(r.text)
        d = soup.find("div", {"id": "resultStats"})
        count = int(d.text.replace("About","").replace("results","").replace(",","").strip())
        mention_count[team] = count


    time.sleep(random.randint(1,3))

print mention_count