from capitals import capitals_dict
import random


def capch():
    vstate, vcity = random.choice(list(capitals_dict.items()))
    while True:
        try:
            uinput = str(input("What is the capital of: {}? if you wanna exit just say it. ".format(vstate)))
            if capitals_dict[vstate] == uinput:
                print("Good! {} is really the capital of {}".format(uinput, vstate))
                break
            elif uinput.lower() =="exit":
                print("Goodbye..BTW the answer was: {}".format(vcity))
                break
            else:
                print("Try again...")
                continue
        except (KeyboardInterrupt, SystemExit):
            print("Goodbye..BTW the answer was: {}".format(vcity))
capch()


