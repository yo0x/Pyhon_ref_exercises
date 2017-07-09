"""
bpath = "/home/y9x/Desktop/test22.txt"
my_lines = open(bpath, "r")
for i in my_lines.readlines():
    print("-2-" "-1-", i),
my_lines.close()

import os
my_path = "/home/y9x/Desktop/files"
file_names_list = os.listdir(my_path)
for file_name in file_names_list:
    if file_name.lower().endswith(".txt"):
        print('Converting {} to JPG...'.format(file_name))
        full_file_name = os.path.join(my_path, file_name)
        new_file_name = full_file_name[0:len(full_file_name)-4] +".jpeg"
        os.rename(full_file_name, new_file_name)
""""
import os

fpath = "/var/home/y9x/Desktop/images/"
file_name_list = os.listdir(fpath)
