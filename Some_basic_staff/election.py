import random

candidatea = 0
candidateb = 0
region1 = 0
region2 = 0
region3 = 0
chanceareg1 = 0.87
chanceareg2 = 0.65
chanceareg3 = 0.17
chancebreg1 = 0.13
chancebreg2 = 0.35
chancebreg3 = 0.83

for i in range(1, 10000):
    ccount = i
    while i == ccount:
        i += 1
        election1 = random.random()

        print(election)
        if i == 10000:
            fregion = print("The winner is".format())
            break
        elif election1 == 2:
            region1 += 1
            continue
        elif election == 3:
            region2 += 1
            continue
        elif election == 4:
            region3 += 1
            continue
        elif election == 2:
            region1 += 1
            continue
        elif election == 3:
            region2 += 1
            continue
        elif election == 4:
            region3 += 1
            continue
        elif election == 2:
            region1 += 1
            continue
        elif election == 3:
            region2 += 1
            continue
        elif election == 4:
            region3 += 1
            continue
        else:
            continue
