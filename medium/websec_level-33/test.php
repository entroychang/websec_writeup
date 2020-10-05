<?php
    $flag = "you did it!!!";

    class B {
        function __destruct() {
            echo "destruct\n";
        }
    }
?>

<?php
    $payload = 'O:9:"Countable":0:{}';
    echo "Going dark…\n";
    ob_start();
    echo "Here is your flag: " . $flag . "\n";
    $a = unserialize($payload);
    ob_end_clean();
?>