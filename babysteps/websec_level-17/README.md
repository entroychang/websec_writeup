# Level 17

1. First, lets check out what is written in http://websec.fr/level17/source.php
2. Then, we would find out a very interesting command :
```
if (! strcasecmp ($_POST['flag'], $flag))
```
3. Since "strcasecmp" is a GREAT command, we can easy hack it XD ~~~
4. So, how it worked? We can find out that if strcasecmp return NULL, then we can get "True" and the flag.
5. What i do is adding [] behind flag and send the request by using Python. Of course using curl or Postman is okay!
6. Here is the flag : WEBSEC{It_seems_that_php_could_use_a_stricter_typing_system}
