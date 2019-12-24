# Level 10

1. First, lets check what is written in http://websec.fr/level10/source.php
2. Then we would found the interesting command below : 
```
 if ($request == $hash) {
    show_source ($file);
} 
```
3. So, all we have to do is try to let PHP compare them as the same by 0 = 0
4. What I do is try to upload file continuely by python and after md5(), it will start "0E", which means "0"
5. Since we are able to control Secret hash value as "0", all we have to do is write a script to help us !
6. Here is the flag : WEBSEC{Lose_typ1ng_system_are_super_great_aren't_them?}
