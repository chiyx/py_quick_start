#! python3

# renameDates.py - Renames filename with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""
    ^(.*?)                      # all text before the date
    ((0|1)?\d)-                # one or two digits for the month
    ([0-3]?\d)-                # one or two digits for the day
    ((19|20)\d\d)               # four digits for the year
    (.*?)$                     # all text after the date
""", re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo is None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(5)
    afterPart = mo.group(7)
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute filepaths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
