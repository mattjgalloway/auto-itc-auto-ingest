#!/usr/bin/python

# auto-itc-auto-ingest
#   Wrapper script to automatically download iTunes Connect sales reports using
#   the auto ingest Java class.
#
#   by Matt Galloway (http://iphone.galloway.me.uk/)
#   see LICENSE and README
#
#   NOTE: THIS IS NOT FINISHED YET! IT WORKS BUT IS NOT EXACTLY CLEAN!

import os
import ConfigParser
import glob
import re
import datetime
import subprocess

def formattedDate(date):
    return date.strftime("%Y%m%d")

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

try:
    username = config.get('creds', 'username')
    password = config.get('creds', 'password')
    vendorid = config.get('creds', 'vendorid')
    filepath = config.get('reports', 'filepath')
    daystoget = config.getint('reports', 'daystoget')
    weekstoget = config.getint('reports', 'weekstoget')
except ConfigParser.NoSectionError, e:
    print e
    exit(1)
except ConfigParser.NoOptionError, e:
    print e
    exit(1)

absfilepath = os.path.abspath(filepath)

startDir = os.getcwd()
os.chdir(absfilepath)

currentDaily = glob.glob('S_D_'+vendorid+'_*')
currentDailyDates = []
for daily in currentDaily:
    dailyFile = os.path.split(daily)[1]
    match = re.search("_(\d+)\.", dailyFile)
    if match:
        currentDailyDates.append(match.group(1))

today = datetime.datetime.now()
previous = today - datetime.timedelta(days=daystoget)
while previous <= today:
    formattedPrevious = formattedDate(previous)
    try:
        (i for i in currentDailyDates if i == formattedPrevious).next()
    except StopIteration, e:
        subprocess.call(["java", "-classpath", startDir, "Autoingestion", username, password, vendorid, "Sales", "Daily", "Summary", formattedPrevious])
    previous += datetime.timedelta(days=1)

currentWeekly = glob.glob('S_W_'+vendorid+'_*')
currentWeeklyDates = []
for daily in currentWeekly:
    weeklyFile = os.path.split(daily)[1]
    match = re.search("_(\d+)\.", weeklyFile)
    if match:
        currentWeeklyDates.append(match.group(1))

previous = today
while previous.weekday() != 6:
    previous -= datetime.timedelta(days=1)

previous -= datetime.timedelta(weeks=weekstoget)
while previous <= today:
    formattedPrevious = formattedDate(previous)
    try:
        (i for i in currentWeeklyDates if i == formattedPrevious).next()
    except StopIteration, e:
        subprocess.call(["java", "-classpath", startDir, "Autoingestion", username, password, vendorid, "Sales", "Weekly", "Summary", formattedPrevious])
    previous += datetime.timedelta(weeks=1)

os.chdir(startDir)
