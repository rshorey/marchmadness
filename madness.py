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

divisions = {"MW":["Virginia","Michigan State","Utah",
    "Iowa State","Purdue","Seton Hall","Dayton",
    "Texas Tech", "Butler","Syracuse","Gonzaga",
    "Little Rock", "Iona", "Fresno", "Tennessee", "Hampton"],

"E":["North Carolina", "Xavier", "West Virginia",
    "Kentucky", "Indiana", "Notre Dame", "Wisconsin",
    "USC", "Providence", "Pittsburgh", "playin-e1",
    "Chattanooga","Stony Brook","Stephen Austin",
    "Weber", "playin-e2"],

"W":["Oregon","Oklahoma","Texas A&M","Duke",
    "Baylor","Texas","Oregon State","St. Joseph's",
    "Cincinnati", "VCU", "UNI", "Yale",
    "Wilmington", "Green Bay", "Bakersfield", "playin-w"],

"S":["Kansas","Villanova","Miami","California",
    "Maryland","Arizona","Iowa","Colorado","Connecticut",
    "Temple","playin-s","South Dakota","Hawaii",
    "Buffalo", "Asheville", "Austin Peay"]
}


base_url = "https://www.google.com/search?client=ubuntu&channel=fs&q=%22march+madness+2016%22+"

playins = {"playin-w":["Holy Cross","Southern"],
            "playin-s":["Vanderbilt","Wichita"],
            "playin-e1":["Michigan","Tulsa"],
            "playin-e2":["FGCU","Fairleigh"]}

#this is for teams that contain another team in their name
#we'll exclude the part that is in the other team's name
#for example, we exclude "state" for plain old Iowa
#to avoid getting Iowa State's results
minuses = {"Iowa":"State",
            "Michigan":"State",
            "Virginia":"West",
            "Oregon":"State",
            "North Carolina":"Asheville+Wilmington",
            "California":"Bakersfield+Fresno",
            "Texas":"Tech+A&M"
            }

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


#mention_count = {'Michigan State': 51100, 'USC': 27600, 'Oklahoma': 73800, "St. Joseph's": 2440, 'Providence': 23100, 'Villanova': 23500, 'UNI': 40900, 'Butler': 69800, 'Indiana': 97900, 'Maryland': 99800, 'playin-e2': 4475.0, 'Temple': 73400, 'Weber': 42600, 'Stony Brook': 14000, 'Iowa': 31100, 'Arizona': 127000, 'Wisconsin': 85000, 'Dayton': 34100, 'Pittsburgh': 62000, 'Oregon State': 10400, 'Kansas': 124000, 'Utah': 69500, 'Virginia': 116000, 'Oregon': 67500, 'Iowa State': 13000, 'Connecticut': 71000, 'Iona': 5440, 'California': 9270, 'Texas': 251000, 'West Virginia': 55500, 'Syracuse': 39000, 'Green Bay': 31700, 'Bakersfield': 8720, 'Chattanooga': 9350, 'Purdue': 29400, 'Miami': 120000, 'Wilmington': 8540, 'Asheville': 7980, 'Little Rock': 8160, 'Hawaii': 118000, 'Kentucky': 97700, 'Baylor': 17300, 'Austin Peay': 2510, 'VCU': 8930, 'Yale': 46000, 'Xavier': 23100, 'Buffalo': 81600, 'Notre Dame': 29200, 'Duke': 107000, 'Stephen Austin': 128, 'Hampton': 32700, 'South Dakota': 19400, 'Cincinnati': 48300, 'Colorado': 142000, 'playin-s': 16400.0, 'Fresno': 18000, 'Seton Hall': 20900, 'playin-e1': 93900.0, 'North Carolina': 89500, 'playin-w': 116775.0, 'Tennessee': 90000, 'Texas A&M': 284000, 'Gonzaga': 8570, 'Texas Tech': 17000}



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









        





