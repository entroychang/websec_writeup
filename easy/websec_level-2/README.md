# Level 2
1. First, lets check what is written in http://websec.fr/level02/source.php
2. Then, we would find that it finally filter those KEYWORDS, so I feel a little bit upset ...
3. BUT until I read the source carefully, I find out that preg_replace will only replace once ! We can get the flag by the command below : 
```
1 uunionnion sselectelect 1, password ffromrom users
```
4. You can think like 1 u~~union~~nion s~~select~~elect 1, password f~~from~~rom users, so it would become : 
```
1 union select 1, password from users
```
5. Here is the flag : WEBSEC{BecauseBlacklistsAreOftenAgoodIdea}
