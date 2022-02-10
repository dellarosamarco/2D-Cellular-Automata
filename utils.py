import random

def setRandomSeed() :
    chars = ["a","b","c","d","e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","v","z","x","y","w","k","j","0","1","2","3","4","5","6","7","8","9"]

    seedLength = random.randint(5,1000)
    seed = ""

    for n in range(0,seedLength) :
        seed += chars[random.randint(0,len(chars)-1)]

    return seed