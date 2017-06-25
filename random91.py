from random import randint

"""
heads = 0
tails = 0
for trial in range(0, 10000):
    while randint(0, 1) == 0:
        tails = tails + 1
    heads  = heads + 1
print ("Heads / tails = ", heads/tails)
"""

dice1 = 0
dice2 = 0
dice3 = 0
dice4 = 0
dice5 = 0
dice6 = 0
for i in range(1, 100000):
    ccount = i
    while i == ccount:
        i += 1
        gdice = randint(1, 6)
        print(gdice)
        if i == 100000:
            fdice = (dice6 + dice5 + dice4 + dice3 + dice2 + dice1) / 6
            print(
                "The average number is: {} there were 1: {}, 2: {}, 3:{}, 4:{}, 5:{}, 6:{}".format(fdice, dice1, dice2,
                                                                                                   dice3, dice4, dice5,
                                                                                                   dice6))
            break
        elif gdice == 2:
            dice2 += 1
            continue
        elif gdice == 3:
            dice3 += 1
            continue
        elif gdice == 4:
            dice4 += 1
            continue
        elif gdice == 5:
            dice5 += 1
            continue
        elif gdice == 6:
            dice6 += 1
            continue
        elif gdice == 1:
            dice1 += 1
            continue
        else:
            continue
