# Level 33

### source code 
```php=
<?php
    include 'flag.php'; //defines $flag

    class B {
      function __destruct() {
        echo "<!-- Almost there? -->";
      }
    }
?>
<?php
    if (isset($_POST['payload'])) {
        echo "Going dark…";
        ob_start();
        echo "Here is your flag: " . $flag . "\n";
        $a = unserialize($_POST['payload']);
        ob_end_clean();
    }
?>
```

### [ob_start](https://www.php.net/manual/zh/function.ob-start.php)
* 在下面的討論中，有一個討論很有趣
    * When a fatal error is thrown, PHP will output the current buffer of Output-Control without postprocessing before printing the error message. If you are working with several output control levels, this might not result in the desired behavior.
    * 簡單來說，如果發生 fatal error，會輸出 buffer 裡面的內容在印出 error message 之前

### [unserialize](https://www.php.net/manual/zh/function.unserialize.php)
* 在題目中，可控的地方只有 unserialize，換句話說，只要 unserialize 造成 fatal error 都可以拿到 buffer 中的內容
* 下面的討論中，有一個討論看起來是關鍵
    * if the serialized string contains a reference to a class that cannot be instantiated (e.g. being abstract) PHP will immediately die with a fatal error.
    * 簡單來說，如果反序列化的對象是抽象類(abstract)，會發生 fatal error
* 那目標就很清楚了，要找一個 object 是預設的，而且是抽象類

### [interface](https://codertw.com/程式語言/109476/)
* 本來想找有沒有 object 是 abstract 的，不過沒找到 ... ╮(╯_╰)╭
* 在 PHP 中，interface 是抽象類，所以只要找在 PHP 中預設的 interface object 就可以了
* 有很多，這是其中的[資料](https://www.php.net/manual/en/spl.interfaces.php)

#### 感謝 @john 大大的幫忙 ヾ(＠゜▽゜@)ノ
