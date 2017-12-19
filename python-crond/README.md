### python-crond() 

is a little piece of code intented to be added into your code to provide time crontrolled launching functions. Its syntax is similar to crontab (see https://linux.die.net/man/5/crontab).

> settings/config.py 

contains the 'Crontab' where you can add your functions and the desired launch time for it. Notice that this file can be edited at the runtime, without the need of stop and relaunch your program.

> crond.py 

is the piece of code to be imported into your scripts to enable cron-like functionality.

> functions.py 

is a file who contains the launching functions.

> usage.py 

is an example of how to integrate cron.py into your scripts.
