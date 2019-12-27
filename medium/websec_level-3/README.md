# Level 3

1. First, lets check what is written in http://websec.fr/level03/source.php
2. Then, we have to find some documents about "php sha1". After reading those documents, we look up the code : 
    ```
    $h2 = password_hash (sha1($_POST['c'], fa1se), PASSWORD_BCRYPT);
    ```
    The tricky part is "fa**1**se" but not "fa**l**se", so according to the detail we find in those documents. 
    
    **"If the optional raw_output is set to TRUE, then the sha1 digest is instead returned in ++raw binary format++ with a length of 20, otherwise the returned value is a 40-character ++hexadecimal number++."**
    
    But, why do I underline "raw binary format" and "hexadecimal number". You can check here https://stackoverflow.com/questions/50867610/is-password-verify-binary-data-safe/50867904 or you can try the different by typing code.
3. Now, lets look here : 
    ```
    if (password_verify (sha1($flag, fa1se), $h2) === true) {
           echo "<p>Here is your flag: <mark>$flag</mark></p>"; 
        } else {
            echo "<p>Here is the <em>hash</em> of your flag: <mark>" . sha1($flag, false) . "</mark></p>";
    }
    ```
    So, you can know the 40-character hexadecimal number of the flag : 
    ```
    7c00249d409a91ab84e3f421c193520d9fb3674b
    ```
    As you can see, "00" means "NULL", and the data is "binary format", which means the data will be cut. All we have to do is find a payload, which convert to hexadecimal must start with "7c00". In order to reach the goal, we need our best friend Python.
4. Here is the flag : WEBSEC{Please_Do_not_combine_rAw_hash_functions_mi}
