import requests
from bs4 import BeautifulSoup
import time
import random



def traverse(div_list):
    div_results = []
    tree = [[[1,16],[2,15],[3,14],[4,13],
            [5,12],[6,11],[7,10],[8,9]],
            [[1,8],[2,7],[3,6],[4,5]],
            [[1,4],[2,3]],
            [[1,2]]]

    prev_list = div_list
    for level in tree:
        print level
        new_list = []
        for game in level:
            team1 = prev_list[game[0]-1]
            team2 = prev_list[game[1]-1]
            winner = play(team1,team2)
            print winner
            new_list.append(winner)

        div_results.append(new_list[:])
        prev_list = new_list
    return div_results 


def play(team1, team2):
    first_count = mention_count[team1]
    second_count = mention_count[team2]
    total = 1.0*(first_count+second_count)
    rand_num = random.random()
    if rand_num <= first_count/total:
        return team1
    return team2

divisions = {"MW":["Kansas","Louisville","Oregon",
    "Purdue","Iowa State","Creighton","Michigan",
    "Miami", "Michigan State","Oklahoma State","Rhode Island",
    "Nevada", "Vermont", "Iona", "Jacksonville", "playin-mw"],

"E":["Villanova", "Duke", "Baylor",
    "Florida", "Virginia", "SMU", "South Carolina",
    "Wisconsin", "Virginia Tech", "Marquette","playin-e1", "Wilmington",
    "East Tennessee","New Mexico State","Troy",
    "playin-e2", "playin-e2"],

"W":["Gonzaga","Arizona","Florida State","West Virginia",
    "Notre Dame","Maryland","St. Mary's","Northwestern",
    "Vanderbilt", "VCU", "Xavier", "Princeton",
    "Bucknell", "Gulf Coast", "North Dakota", "South Dakota"],

"S":["UNC","Kentucky","UCLA","Butler",
    "Minnesota","Cincinnati","Dayton","Arkansas","Seton Hall",
    "Wichita","playin-s","Middle Tennessee","Winthrop",
    "Kent State", "Northern Kentucky", "Texas Southern"]
}


base_url = "https://www.google.com/search?client=ubuntu&channel=fs&q=%22march+madness+2017%22+"

playins = {"playin-mw":["NC Central","UC Davis"],
            "playin-s":["Kansas State","Wake Forest"],
            "playin-e1":["Providence","USC"],
            "playin-e2":["Mount St. Mary","New Orleans"]}

#this is for teams that contain another team in their name
#we'll exclude the part that is in the other team's name
#for example, we exclude "state" for plain old Iowa
#to avoid getting Iowa State's results
minuses = {
            "Michigan":"State",
            "Virginia":"Tech+West",
            "Florida":"Gulf",
            "Tennessee":"East+Middle",
            "Kentucky":"Northern",
            "Texas":"Southern",
            "Florida":"State",
            "Kansas":"State",
            }
"""
mention_count = {}
for div,teams in divisions.items():
    for team in teams:
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
            
        else:
            if team in minuses:
                print base_url+"%22"+team+"%22"+"+-"+minuses[team]
                r = requests.get(base_url+"%22"+team+"%22"+"+-"+minuses[team])
            
            else:
                r = requests.get(base_url+"%22"+team+"%22")
            soup = BeautifulSoup(r.text)
            d = soup.find("div", {"id": "resultStats"})
            count = int(d.text.replace("About","").replace("results","").replace(",","").strip())
            mention_count[team] = count
            

        time.sleep(random.randint(1,3))

print mention_count
"""
mention_count = {'Princeton': 10200, 'Michigan State': 15500, 'East Tennessee': 5660, 'SMU': 12300, 'Minnesota': 59700, 'Middle Tennessee': 7690, 'Louisville': 21700, 'Villanova': 62700, 'Arkansas': 28800, 'Vanderbilt': 18200, 'Xavier': 9890, 'Butler': 19500, 'Maryland': 71100, 'playin-s': 13700.0, 'Gulf Coast': 6240, 'Bucknell': 4420, 'Oklahoma State': 8410, 'Wisconsin': 64200, 'Arizona': 104000, 'playin-e1': 19600.0, 'Michigan': 58500, 'Kansas': 43500, 'Wilmington': 7670, 'Virginia': 12100, 'Oregon': 36400, 'Notre Dame': 33400, 'Florida State': 13800, 'West Virginia': 21100, 'South Carolina': 21100, 'Northern Kentucky': 4110, 'Jacksonville': 22800, 'Northwestern': 50100, 'Vermont': 13500, 'North Dakota': 7190, 'Wichita': 13800, 'Purdue': 14700, 'Miami': 82700, 'playin-mw': 5715.0, 'Florida': 16700, 'Kentucky': 36000, 'Rhode Island': 14000, 'Baylor': 15300, 'UNC': 44500, "St. Mary's": 9030, 'Kent State': 7300, 'New Mexico State': 2910, 'playin-e2': 26330.0, 'South Dakota': 5150, 'Iowa State': 21600, 'Creighton': 13200, 'Duke': 96400, 'Texas Southern': 4800, 'Cincinnati': 28800, 'Winthrop': 7630, 'Seton Hall': 10000, 'Dayton': 14400, 'UCLA': 98400, 'Troy': 17300, 'Iona': 5620, 'Gonzaga': 52500, 'Marquette': 10200, 'Nevada': 13000, 'Virginia Tech': 11300, 'VCU': 16400}


#up to final four
results = {}
for div,teams in divisions.items():
    print div
    results[div] = traverse(teams)

print results
#final four
f1 = play(results["MW"][-1][0],results["E"][-1][0])
f2 = play(results["S"][-1][0],results["W"][-1][0])

print "\nfinal four"
print f1
print f2

winner = play(f1,f2)
print "\nfinals"
print winner









        





