import argparse
import re

ap = argparse.ArgumentParser()
ap.add_argument('-lf', '--lum_file', required = True, help = 'Path to lum file')
ap.add_argument('-tf', '--temp_file', required = True, help = 'Path to temp file')
args = vars(ap.parse_args())

## define regexes
# group 1: hour
# group 2: luminosity
# lum entry example:  2016-09-21_17-29-43.png 96.1040781279
lum_entry_pat  = r'.*\d+-\d+-\d+_(\d+)-\d+-\d+\.png\s+(\d+\.\d+)'
# temp entry example: 2016-09-21_17-29-44 31.0
temp_entry_pat = r'.*\d+-\d+-\d+_(\d+)-\d+-\d+\s+(\d+\.\d+)'

## define two dictionaries
lum_tbl = {}
tmp_tbl = {}

with open(args['lum_file']) as infile:
    for line in infile:
        m = re.match(lum_entry_pat, line)
        if m != None:
            hour = m.group(1)
            lum = float(m.group(2))
            if hour in lum_tbl.keys():
                lum_tbl[hour].append(lum)
            else:
                lum_tbl[hour] = [lum]

with open(args['temp_file']) as infile:
    for line in infile:
        m = re.match(temp_entry_pat, line)
        if m != None:
            hour = m.group(1)
            tmp = float(m.group(2))
            if hour in tmp_tbl.keys():
                tmp_tbl[hour].append(tmp)
            else:
                tmp_tbl[hour] = [tmp]

## print tables and averages
print('Luminosity Table')
for h, lums in sorted(lum_tbl.items()):
    print h, '-->', str(lums)
print

print('Temperature Table')
for h, temps in sorted(tmp_tbl.items()):
    print h, '-->', str(temps)
print

print('Luminosity Averages')
for h, lums in sorted(lum_tbl.items()):
    print h, '-->', sum(lums)/len(lums)
print

print('Temperature Averages')
for h, temps in sorted(tmp_tbl.items()):
    print h, '-->', sum(temps)/len(temps)
print
