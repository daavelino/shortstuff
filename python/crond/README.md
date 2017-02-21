crond() is a python 3 scripts intented to be added into your code to provide time crontrol when lauch functions. Its syntax is similar to crontab (see https://linux.die.net/man/5/crontab)

- settings/config.py contains the 'Crontab' where you can add your functions and the desired launch time for it. Notice that this file can be edited at the runtime, without the need of stop and relaunch your program.

- crond.py is the piece of code to be added into your scripts to enable cron-like functionality.

- usage.py is an example of how to integrate cron.py into your scripts.

- functions.py is a file who contains the launching functions.
