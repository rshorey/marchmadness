import random

nouns = ["team","bracket","code","github account",
        "database","algorithm","free throw percent",
        "point guard","mascot","t-shirt cannon"]

adjectives = ["stinky","small","hackable",
                "dastardly","Machiavellian",
                "irresponsible","serpentine",
                "deflated","a loser","going down",
                "doomed","flat-footed"]

noun = random.choice(nouns)
adj = random.choice(adjectives)
print "Your {noun} is {adjective}.".format(noun=noun,adjective=adj)