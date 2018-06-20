import os
import glob

vpath = "/home/y9x/desktop/images"
poss_f = os.path.join(vpath, "*.jpeg")

for file in glob.glob(poss_f):
    if os.path.getsize(file) >= 2000:
        print("{} is bigger or iqual to 2000 bites killing it!")
        os.remove(file)
    else:
        print("{} is not big.".format(file))
