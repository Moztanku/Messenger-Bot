from fbchat import  Client
from fbchat.models import *
import sched
import datetime
import time
import random

ids = [
#PUT YOUR FRIENDS MESSENGER IDS HERE IN ' ' ex. '100003394556677', they will always start with 10000, you can get them simply
#by inspecting element on messenger and looking for "buddy_id": , your own uid is where "USER_ID":
]

night_prefix = ['Dobranoc ',
          'Branoc ',
          'Dobrej nocy ',
          'Dobranoooc ',
          'DOBRANOC ']
night_sufix = ['!',
         ' <3',
         ' ;>',
         ' ^w^',
         ' c;',
         ' :-)',
         ' Przyjacielu!',
         ' Kolego']
day_prefix = ['Dzień dobry ',
                'Dobrego dnia ',
                'Dobry dzień ',
                'Miłego dnia ',
                'Udanego dnia ']
day_sufix = [' !',
               ' :)',
               ' <3',
               ' c;',
               ' ;>',
               ' Przyjacielu!',
               ' Kolego']
client=Client("YOUR_EMAIL ","YOUR_PASSWORD")
client.send(Message('STARTED'), thread_id=client.uid, thread_type=ThreadType.USER)
var = True
while var == True:
    if(time.gmtime().tm_sec == 00
    and time.gmtime().tm_min == 00
    and time.gmtime().tm_hour == 22):
        for x in ids:
            user = client.fetchUserInfo(x)[x]
            interfix = user.first_name
            client.send(Message(text=night_prefix[random.randrange(len(night_prefix))]+interfix+night_sufix[random.randrange(len(night_sufix))]), thread_id=x, thread_type=ThreadType.USER)
            time.sleep(1)
        var = False
var = True
while var == True:
    if(time.gmtime().tm_sec == 00
    and time.gmtime().tm_min == 00
    and time.gmtime().tm_hour == 8):
        for x in ids:
            user = client.fetchUserInfo(x)[x]
            interfix = user.first_name
            client.send(Message(text=day_prefix[random.randrange(len(day_prefix))]+interfix+day_sufix[random.randrange(len(day_sufix))]), thread_id=x, thread_type=ThreadType.USER)
            time.sleep(1)
        var = False
client.logout()
