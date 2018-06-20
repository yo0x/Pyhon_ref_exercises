import os
import glob
vpathli = "/home/y9x/Desktop/images/text.txt"
vpathli2 = "/home/y9x/Desktop/images/text2.txt"
vpathli3 = "/home/y9x/Desktop/images/"

with open(vpathli, "r") as my_inputf, open(vpathli2, "w") as my_outputf:
    for line in my_inputf.readlines():
        my_outputf.writelines(line)
        print(line)
my_inputf.close()
my_inputf = open(vpathli2, "r")
my_inputf.seek(5, 0)
print("Line 2", my_inputf.readline())
vpathlist = os.listdir(vpathli3)
print(vpathlist)
for folder in vpathlist:
    full_path = os.path.join(vpathli3, folder)
    if os.path.isdir(full_path):
        os.rename(full_path, full_path + " Folder")
print("-----------------------___------------------------------------------")
print("1:")
for files in vpathlist:
    print(os.path.join(vpathli3, files))
print("2: ")
poss_f = os.path.join(vpathli3, "*/*.jpeg")
for files2 in glob.glob(poss_f):
    print(files2)
print("3: ")
