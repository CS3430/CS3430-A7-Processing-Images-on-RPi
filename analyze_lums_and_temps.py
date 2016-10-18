import argparse
import cv2
import sys
import os
import fnmatch
import re

ap = argparse.ArgumentParser()
ap.add_argument('-lf', '--lum_file', required = True, help = 'Path to lum file')
ap.add_argument('-tf', '--temp_file', required = True, help = 'Path to temp file')
args = vars(ap.parse_args())

## define regexes
lum_entry_pat  = r''
temp_entry_pat = r''

## define two dictionaries
lum_tbl = {}
tmp_tbl = {}

with open(args['lum_file']) as infile:
    for line in infile:
        m = re.match(lum_entry_pat, line)
        if m != None:
            ## your code to fill up lum_tbl

with open(args['temp_file']) as infile:
    for line in infile:
        print line
        m = re.match(temp_entry_pat, line)
        if m != None:
            ## your code to fill up tmp_tbl

## print tables and averages
print('Luminosity Table')
for h, lums in lum_tbl.items():
    print h, '-->', str(lums)
print

print('Temperature Table')
for h, temps in tmp_tbl.items():
    print h, '-->', str(temps)
print

print('Luminosity Averages')
for h, lums in lum_tbl.items():
    print h, '-->', sum(lums)/len(lums)
print

print('Temperature Averages')
for h, temps in tmp_tbl.items():
    print h, '-->', sum(temps)/len(temps)
print



       


    

