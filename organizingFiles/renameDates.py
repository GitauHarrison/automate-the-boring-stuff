#!python3
# renameDates.py - Renames files with American style MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

# Create a regex that matches with the American date format
datePattern = re.compile(r'''^(.*?) # all the text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
''',re.VERBOSE)

#TODO:  Loop over the files in the working directory
# Loop over the files in the working directory
for amerFilename in os.listdir('/home/gitau/Software Development'):
    mo = datePattern.search(amerFilename)

    #skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


#TODO: Form the European-style filename


#TODO: Get the full, absolute paths


#TODO: Rename the files