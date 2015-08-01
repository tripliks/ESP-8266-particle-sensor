import serial, requests, re, csv, os
from datetime import datetime

ser = serial.Serial(1,timeout=4)

datafile = 'arduino data.csv'
P2ratio = None
if not os.path.isfile(datafile):
    with open(datafile,'a+') as csvfile:
        arduinocsv = csv.writer(csvfile, delimiter = ',')
        arduinocsv.writerow(['0.5um', '1um', 'time (iso)'])

with open(datafile,'a+') as csvfile:
    arduinocsv = csv.writer(csvfile, delimiter = ',')
    while True:
        line = ser.readline()
        if line!='':
            print line
            if re.search('.*P1: (\d+\.\d+).*', line):
                P1conc = re.search('.*P1: (\d+\.\d+).*', line).group(1)
            if re.search('.*P1 ratio: (\d+\.\d+).*', line):
                P1ratio = re.search('.*P1 ratio: (\d+\.\d+).*', line).group(1)
            if re.search('.*P2: (\d+\.\d+).*', line):
                P2conc = re.search('.*P2: (\d+\.\d+).*', line).group(1)
            measureTime = datetime.now().isoformat()
            if re.search('.*P2 ratio: (\d+\.\d+).*', line) and P2ratio != None:
                print '.*P1, P2 ratios:.*', P1ratio, P2ratio
                print '.*P1, P2 concs:.*', P1conc, P2conc
                P2ratio = re.search('.*P2 ratio: (\d+\.\d+).*', line).group(1)
                arduinocsv.writerow([P2ratio, P1ratio, measureTime])