# watchlistcalender
A personal movie or tvshow watched calender using python. 
Initially some random testing code. 
After a full functioning raw code my plan is to convert this hole project to a full responsive calender program. 
currently thinking about flask and django. Although I have to learn it. 
##### Questions I have now:
- [x] How to i send this data to my google calender ? (maybe Google calender api!) 
     ##### New problem arise:
     - [ ] Although i am able to push my watched episode to calender but i am only 
able to send the system current time, I need to learn how can i pass the actual playing time 
and playing duration time. So that if my script sun at the middle of the episode it will grab the start time and actual ending time and send those
to google calender. 
* Should i store those to a database or i just send them on the fly ? 
* From when to when I watched that episode and add those entry to my google calender event! (maybe i should use kodis default request parameter)
* Re structure the folder stucture like this. 
```
Project/
    |-- bin/
    |   |-- project
    |
    |-- project/
    |   |-- test/
    |   |   |-- __init__.py
    |   |   |-- test_main.py
    |   |   
    |   |-- __init__.py
    |   |-- main.py
    |
    |-- setup.py
    |-- README
```
##### Currently my program can do:
* Retrive what is playing on my kodi and display them as playing {Serise Name} {Serise season} {Episode}
* User authanication using google api
* Push retrived data to google calender using the api. With system time.

#### Things i did not include to the repo:
* Api credentials.json and token.pickle :)  