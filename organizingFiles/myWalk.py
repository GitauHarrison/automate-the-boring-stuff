import os

for folderName, subfolderNames, fileNames in os.walk('/home/gitau/Software Development/python/automateTheBoringStuff/organizingFiles'):
    print('The current folder is ' + folderName + '\n\n')

    for subfolder in subfolderNames:
        print('SUBFOLDER of ' + folderName + ': ' + subfolder + '\n\n')

    for fileName in fileNames:
        print('FILE INSIDE ' + folderName + ': ' + fileName + '\n\n')
