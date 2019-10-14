#!python3
# backupToZip.py - copies an entire folder and its contents
# to a ZIP file whose filename increments

import os, zipfile

def backupToZip(folder):

    # backup the entire contents of 'folder' into a zip file

    #make sure the folder is absolute
    folder = os.path.abspath(folder)

    # name your files appropriately
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    # Creating the ZIP file
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the entire tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' %(foldername))

        # Add the current folder to the ZIP file
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('/home/gitau/Software Development/python/automateTheBoringStuff/organizingFiles')