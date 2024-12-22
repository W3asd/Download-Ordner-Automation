# Import the libraries
from os import listdir
from os.path import isfile, join
import os
import shutil


file_path = "D:/Downloads"

files = [ f for f in listdir(file_path) if isfile(join(file_path, f)) ]

extension_list = []
extension_dict = {}

for file in files:

    extension = file.split(".")[1]

    if extension not in extension_list:

        extension_list.append(extension)
        
        new_folder_name = file_path + "/" + extension + "_folder"

        extension_dict[str(extension)] = str(new_folder_name)

        if os.path.isdir(new_folder_name) == True:
            continue

        else:
            os.mkdir(new_folder_name)

for file in files:
        
    src_path = file_path + "/" + file
    extension = file.split(".")[1]
        
    if extension in extension_dict.keys():
        
        dest_path = extension_dict[str(extension)]

        shutil.move(src_path, dest_path)

     

