import random

nouns = ["team","bracket","code","github account"]

adjectives = ["stinky","small","hackable"]

noun = random.choice(nouns)
adj = random.choice(adjectives)
print "Your {noun} is {adjective}.".format(noun=noun,adjective=adj)