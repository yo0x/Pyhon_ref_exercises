from random import randint


trials = 10000
flips = 0

for i in range(1, trials):
    trial = randint(0, 1)
    flips +=1
    btrial = trial
    while trial == btrial:
        trial = randint(0, 1)
        if trial != btrial:
            flips +=1
            aaverage = flips / trials
            print ("Average flips was: {}".format(aaverage))
            break
        else:
            flips += 1
            continue