"""
bpath = "/home/y9x/Desktop/test22.txt"
my_lines = open(bpath, "r")
for i in my_lines.readlines():
    print("-2-" "-1-", i),
my_lines.close()
"""
bpath = "/home/y9x/Desktop/test22.txt"
with open(bpath, "r") as my_lines2:
    for line in my_lines2.readlines():
        print(line)
