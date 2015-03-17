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

divisions = {"MW":["Kentucky","Kansas","Notre Dame",
    "Maryland","West Virginia",
    "Butler","Wichita","Cincinnati",
    "Purdue","Indiana","Texas",
    "Buffalo","Valparaiso","Northeastern",
    "New Mexico","playin-mw"],

"E":["Villanova","Virginia","Oklahoma",
    "Louisville","Iowa","Providence",
    "Michigan State","NC State","LSU","UGA",
    "playin-e","Wyoming","Irvine",
    "Alabama","Belmont","Lafayette"],

"W":["Wisconsin","Arizona","Baylor",
    "UNC","Arkansas","Xavier",
    "VCU","Oregon","Oklahoma State",
    "Ohio","playin-w",
    "Wofford","Harvard","Georgia State",
    "Texas Southern","Costal Carolina"],

"S":["Duke","Gonzaga","Iowa State","Georgetown",
    "Utah","Methodist","Iowa",
    "San Diego","St John","Davidson",
    "UCLA","Austin","Washington",
    "UAB","North Dakota","playin-s"]
}

base_url = "https://www.google.com/search?client=ubuntu&channel=fs&q=%22march+madness+2015%22+"

playins = {"playin-w":["BYU","Ole Miss"],
            "playin-s":["Hampton","Manhattan"],
            "playin-e":["Boise","Dayton"],
            "playin-mw":["New Hampshire","NJIT"]}

#this is for teams that contain another team in their name
#we'll exclude the part that is in the other team's name
#for example, we exclude "state" for plain old Iowa
#to avoid getting Iowa State's results
minuses = {"Iowa":"State",
            "Georgia":"State",
            "Texas":"Southern",
            "Oklahoma":"State"}


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
                r = requests.get(base_url+"%22"+team+"%22"+"+-"+minuses[team])
            else:
                r = requests.get(base_url+"%22"+team+"%22")
            soup = BeautifulSoup(r.text)
            d = soup.find("div", {"id": "resultStats"})
            count = int(d.text.replace("About","").replace("results","").replace(",","").strip())
            mention_count[team] = count


        time.sleep(random.randint(1,3))



print mention_count


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









        





