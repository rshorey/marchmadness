import random

nouns = ["team","bracket","code","github account",
        "database","algorithm"]

adjectives = ["stinky","small","hackable",
                "dastardly","Machiavellian",
                "irresponsible"]

noun = random.choice(nouns)
adj = random.choice(adjectives)
print "Your {noun} is {adjective}.".format(noun=noun,adjective=adj)