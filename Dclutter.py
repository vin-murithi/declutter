import os
from posixpath import split
from collections import defaultdict
from  pprint import pprint

#Locate the folder to declutter.
DESKTOP_PATH = os.path.join(os.path.expanduser('~'), 'Desktop')
DESKTOP_PATH2 = os.path.join(DESKTOP_PATH, 'DESKTOP')

# Loop through the file items in the Desktop directory and add them to a DefaultDict
file_mappings = defaultdict()
files = os.listdir(DESKTOP_PATH)
stop = '.'
for file in files:
    if file == 'Dclutter.exe':
        continue
    if stop in file:
        folder = file.split('.')[-1]    #split and take the extension as the folder name.
        folder = str(folder)            #make the extension into a string
        file_mappings.setdefault(folder.upper(), []).append(file) #add to the defaultdict using setdefault, append file

# Create folder for each file type & Move the files to their folders.
for folder, files in file_mappings.items(): #for every folder and file in the file_mappings dictionary
    folder = os.path.join(DESKTOP_PATH2, folder) #create the path name of the folder in the new DESKTOP folder.
    if os.path.isdir(folder) == False:          #Check if file doesnt exist
        os.mkdir(folder)                        #create the folder
    for file in files:
        source = os.path.join(DESKTOP_PATH, file) #find the file
        destination = os.path.join(folder, file)  #create file destination path
        os.rename(source, destination)              #move the file to destination.

#Move folders into the DESKTOP folder
folders = os.listdir(DESKTOP_PATH)
for folder in folders:
    if folder == 'DESKTOP':
        continue
    source = os.path.join(DESKTOP_PATH, folder)
    destination = os.path.join(DESKTOP_PATH2, folder)
    os.rename(source, destination)