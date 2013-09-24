import urllib2
import re

response = urllib2.urlopen('http://www.iluohe.com/city/zhejiang/hangzhou/')
html = response.read()

p = re.compile(r'>(\d{7})<')
numbers = p.findall(html)

output = open('hangzhou_phone_dict.txt', 'a')
for n in numbers:
    n = n + '0000'
    aNum = long(n)
    tempdict = ''
    for i in range(0,10000):
        tempdict += str(aNum + i) + '\n'
    output.write(tempdict)
    output.flush()
    
output.close()