# Level 22

1. First, lets check what is written in http://websec.fr/level22/source.php
2. Then, we would find a blacklist and it is sad that we can not use commands which are in the list. So we have to check the list and find what command we want.
3. Now, we have to check what is in the list. Lets look up the command below : 
    ```
    if ($insecure) {
        echo 'Insecure code detected!';
    } else {
        eval ("echo $code;");
    }
    ```
    To be brief, if we type anything in the blacklist, we can't do anything. But we can type
    ```
    echo '$blacklist{0}';
    ```
    Inorder to check the first command of the blacklist and the result is : 
    ```
    func_num_args
    ```
    Since it is a huge number, we need our best friend Python to help us.
4. After we know how to check, next step, we have to know what command we need to dump the value we need and where to dump. So, after search on the web with keywords "dump data php", we are able to find the command "var_dump" easily.
5. Now, we have to know where we would like to dump the flag. Lets check the code below : 
    ```
    class A {
        public $pub;
        protected $pro ;
        private $pri;

        function __construct($pub, $pro, $pri) {
            $this->pub = $pub;
            $this->pro = $pro;
            $this->pri = $pri;
        }
    }

    include 'file_containing_the_flag_parts.php';
    $a = new A($f1, $f2, $f3);
    ```
    So, we know that "$a" is the place where we want to dump the data.
6. The final step, lets think of a payload that can dump all the data from "$a" : 
    ```
    var_dump($a)
    ```
    Since we cannot type any of the command in the blacklist, we can use the payload below 
    ```
    $blacklist{a number}($a) == var_dump($a)
    ```
    Then, we can get our flag ~~~
7. Here is the flag : WEBSEC{But_I_was_told_that_OOP_was_flawless_and_stuff_:<}
