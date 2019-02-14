import urllib.request as req
import csv

url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'

f = req.urlretrieve(url, url.split('/')[-1])[0]

stat = {}
with open(f) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    for row in reader:
        AAR, BYDEL, ALDER, STATKODE, PERSONER = [int(x) for x in row]
        stat.setdefault(AAR,{})
        stat[AAR].setdefault(BYDEL,{})
        stat[AAR][BYDEL].setdefault(ALDER,{})
        stat[AAR][BYDEL][ALDER].setdefault(STATKODE,PERSONER)
