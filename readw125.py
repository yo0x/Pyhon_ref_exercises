vpathli = "/home/y9x/Desktop/images/text.txt"
vpathli2 = "/home/y9x/Desktop/images/text2.txt"
with open(vpathli, "r") as my_inputf, open(vpathli2, "w") as my_outputf:
    for line in my_inputf.readlines():
        my_outputf.writelines(line)
        print(line)
my_inputf.close()
