import urllib.request
import json
import datetime
from collections import Counter
b = []
x1 = datetime.datetime.now()
print("Η ΜΕΡΑ ΣΗΜΕΡΑ ΕΙΝΑΙ:", x1.strftime("%d"),"-",x1.strftime("%m"), "-", x1.strftime("%y"))
for i in range(1, int(x1.strftime("%d"))+1):

    c = datetime.datetime(2021, int(x1.strftime("%m")), i)
    year = x1.strftime("%Y")
    day = c.strftime("%d")
    month = x1.strftime("%m")
    url2 = "https://api.opap.gr/draws/v3.0/1100/draw-date/"+year+"-"+month+"-"+day+"/"+year+"-"+month+"-"+day+"/draw-id"
    r2 = urllib.request.urlopen(url2)
    html2 = r2.read()
    html2 = html2.decode()
    data2 = json.loads(html2)

    firstdraw = str(data2[0])

    url1 = "https://api.opap.gr/draws/v3.0/1100/"+firstdraw
    r1 = urllib.request.urlopen(url1)
    html1 = r1.read()
    html1 = html1.decode()
    data1 = json.loads(html1, strict=False)
    a = data1["winningNumbers"]['list']
    print(data2[0])
    print(a)

    b.append(a)
c = b[0]
for i in range(1, int(x1.strftime("%d"))):
    c.extend(b[i])
keys_1 = list(Counter(c).keys())
len(keys_1)
values_1 = list(Counter(c).values())
for i in range(0, len(keys_1)):
    print("Ο ΑΡΙΘΜΟΣ", keys_1[i], "ΕΜΦΑΝΙΖΕΤΑΙ", values_1[i], "ΦΟΡΕΣ")