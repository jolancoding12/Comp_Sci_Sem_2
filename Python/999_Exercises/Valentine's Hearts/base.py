import random
ppllist = ["squirrel", "chick from squid game","jesus", "kayne", "borther", "senor poole", "kool-aid man", "joe biden"]
complist = [" is yummy", " packing", " smells like rust.", " is cool", " is poggers", " hates dinosaurs", " has a third cousin twice removed", " taught their kid the enirety of the star wars prequel trilogy"]

poeple = random.randrange(0,len(ppllist))
comp = random.randrange(0,len(complist))

print(ppllist[poeple] + complist[comp])