# install

1. get latest version of python (>3.8)
2. get chromedriver.exe (https://chromedriver.chromium.org/) and add it to PATH
3. `pip install selenium`
4. `pip install beautifulsoup4`

# running

1. edit config.py and add your reddit username and password
2. warning: it could crash chrome, so save important stuff first
3. warning: it may take a while to start because each driver needs to login first
4. `python main.py`

# expected output

```
[T4196]: loaded 101 users from db
[T1336]: scraping r/all
[T1336]: scraping r/aww
[T9140]: searching thread "(9) Dogs getting caught :.." for cakes
[T9124]: searching thread "(9) TIL That in 2007, Roc.." for cakes
[T9132]: searching thread "(9) The note George HW Bu.." for cakes
[T8576]: searching thread "(9) Alex Trebek’s wife of.." for cakes
[T1336]: scraping r/videos
[T9140]: searching thread "(9) America's top militar.." for cakes
[T1336]: scraping r/Jokes
[T8576]: adding user "charm59801" to the queue
[T8576]: adding user "causewaynoway" to the queue
[T8576]: adding user "Cereborn" to the queue
[T8576]: adding user "Krakathulhu" to the queue
[T8576]: adding user "mageta621" to the queue
[T8576]: adding user "deathislit" to the queue
[T8576]: adding user "HolyShatner" to the queue
[T8576]: adding user "mockingseagull" to the queue
[T1336]: scraping r/ThatsInsane
[T9128]: replying to post "t1_gc4q45y" made 1 hour ago
[T8576]: searching thread "(9) tonight this guy drov.." for cakes
[T1336]: scraping r/dataisbeautiful
[T9132]: adding user "Junkiebuttpiss" to the queue
[T9132]: adding user "PrisAustin" to the queue
[T9132]: adding user "berserkergandhi" to the queue
[T9128]: replying to post "t1_gc4oo0j" made 1 hour ago
[T8576]: adding user "oxymoronix" to the queue
[T8576]: adding user "the_great_philouza" to the queue
[T8576]: adding user "firemaycrie" to the queue
[T9132]: searching thread "(9) It’s called game desi.." for cakes
```