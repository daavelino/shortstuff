import time
import datetime
import copy

from settings.config import *
from functions import print_1, print_2 

def run(function):
    eval(function)

def crond():

    now = list() 
    tmp = datetime.datetime.now()
    now.append(tmp.minute)
    now.append(tmp.hour)
    now.append(tmp.day)
    now.append(tmp.month)
    now.append(tmp.weekday())

    #### Parsing config.py file:
    fraction = 0
    tmp = copy.deepcopy(CRONTAB)
    crontab = list()
    for i in tmp:
        sched = i[0]
        sched = sched.split()
        sched.append(i[1])
        crontab.append(sched)

    for entry in crontab:
        for i in range(0, len(now)):
            entry[i] = entry[i].replace('*', str(now[i])) 
            if '/' in entry[i]:
                fraction = entry[i].split('/')
                fraction = int(fraction[0]) % int(fraction[1])
                if fraction == 0: # They are multiples each other.
                    entry[i] = int(now[i])
                else:
                    entry[i] = -1 # here to never match.
             
            entry[i] = int(entry[i])

        if entry[0:5] == now:
            run(entry[-1])

    time.sleep(60)

