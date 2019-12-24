# Level 11

1. First lets us check what is written in http://websec.fr/level11/source.php
2. Then we could easily find out that it filter lots of words and special marks and we could not type in user_id because it could only receive numbers.
3. What I do is sending the special table using Python. Below is my payload : 
```
(select 2 id,enemy username from costume where id like 1)
```
4. If we place it in the whole command : 
```
$query = 'SELECT id,username FROM ' . (select 2 id,enemy username from costume where id like 1) . ' WHERE id = ' . 2;
```
5. Then we come up another question, why and how I write the payload. We have to get the value from table. However we can not use UNION JOIN AS to get value, we have to change the table where we would like to search. Finally we can select 2 and id, enemy's username from the table costume where id like (is) 1 as table.
6. Here is the flag : WEBSEC{Who_needs_AS_anyway_when_you_have_sqlite}
