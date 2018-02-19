########
#### setup.py: script to build and help developent of the Vulnerability catalog.
#### Date: 2018-02-18
#### Version: 1.0
#### Author: Daniel Avelino https://daavelino.github.io
########

import platform
import sys
import pprint
import shutil
from pathlib import Path
import os

global MINIMAL_PYTHON_VERSION
global MINIMAL_DJANGO_VERSION
global PROJECT_NAME
global APP_NAME

MINIMAL_PYTHON_VERSION = (3,0)
MINIMAL_DJANGO_VERSION = (2,0)
PROJECT_NAME="base"
APP_NAME="catalog"

######## System properties:
def get_environment():
    '''Returns a dictionary with relevant information about OS environment'''
    env = dict()
    env['system'] = platform.system()

    if env['system'] == 'Linux':
        env['system version'] = platform.linux_distribution()
    
    if env['system'] == 'Windows':
        env['system version'] = platform.linux_distribution()

    return(env)

def check_parameters():
    allowed_params = {
        'build': "setup and builds the project from the scratch.",
        'clean': "remove all project related files.",
        'deep-clean': "remove all project related files and venv structure.",
        'help': "prints a help message.",
        'loadvenv': "creates a functional Python's Virtual Environment at current directory.",
        'templates': "updates project's Templates, forms and static files only.",
        'urlsviews': "updates project's Urls and Views only."
        
    }

    if (len(sys.argv) == 2) and (sys.argv[1] in allowed_params.keys()): # one and only one allowed parameter has to be passed.
        param = sys.argv[1] # Because argv[0] is the file name.
        return param
    else:
        print("\nUsage:", sys.argv[0], "<options>, where <options> are:\n")
        for i in allowed_params.items():
            print("  " + i[0] + ":    " + i[1])
        print("\nExiting.")
        sys.exit(1)
        
def load_venv():
    target = Path('./venv')
    env = get_environment()
    
    if not target.is_dir():
        os.makedirs(target)
        if env['system'] == 'Linux':
            os.system('python3 -m venv venv') # creating venv.
            print("\n[Warning]")
            print("Virtual Environment not load yet. Please, load venv by running:")
            print("\n    source venv/bin/activate\n")
            print("and run setup.py script again.")
        if env['system'] == 'Windows':
            os.system('python.exe -m venv venv') # creating venv.
            print("\n[Warning]    Virtual Environment not load yet. Please, load venv by running:")
            print("\n    venv\\Scripts\\activate.bat\n")
            print("and run setup.py script again.")
        sys.exit(1)       
    else:
        if not "venv" in sys.prefix: # venv is not loaded:
            if env['system'] == 'Linux':
                print("\n[Warning]")
                print("Virtual Environment not load yet. Please, load venv by running:")
                print("\n    source venv/bin/activate\n")
                print("and run setup.py script again.")
            if env['system'] == 'Windows':
                print("\n[Warning]")
                print("Virtual Environment not load yet. Please, load venv by running:")
                print("\n    venv\\Scripts\\activate.bat\n")
                print("and run setup.py script again.")
            sys.exit(1)
        else:
            pass

def check_system_reqs():
    '''It will not run until all dependencies have been filled'''
    env = get_environment()
    #### Checking Python version:
    python_version = sys.version_info
    if python_version < MINIMAL_PYTHON_VERSION:
        print("\n[Warning]    Missing Python " \
              + str(MINIMAL_PYTHON_VERSION[0]) + "." \
              + str(MINIMAL_PYTHON_VERSION[1]) \
              + " (or greater) version.\n")
        print("Please, upgrade Python first (https://www.python.org/downloads/).\nExiting.\n")
        sys.exit(1)

    #### Check if pip is installed:
    try:
        import pip
    except ImportError: # Exit, since it is a required dependency.
        print("\n[Warning]    Missing pip.\n")
        print("Please, install it first (https://pip.pypa.io).\nExiting.\n")
        sys.exit(1)


    #### Check if Django is installed (if not, install it properly):
    try: 
        from django.core.management import execute_from_command_line
    except ImportError: # so, install it properly:
        print("\n[Warning]    Missing Django.\n")
        if env['system'] == 'Linux':
            print("Using\n\n    pip3 install django\nto fix this dependency...\n")
            os.system("pip3 install django>=" \
                      + str(MINIMAL_DJANGO_VERSION[0]) \
                      + "." \
                      + str(MINIMAL_DJANGO_VERSION[1]))
            print("Done.")
        if env['system'] == 'Windows':
            print("Using\n\n    pip.exe install django\nto fix this dependency...\n")
            os.system("pip.exe install django>=" \
                      + str(MINIMAL_DJANGO_VERSION[0]) \
                      + "." \
                      + str(MINIMAL_DJANGO_VERSION[1]))
            print("Done.")

    #### Check Django version:
    #### We opt not to update Django version here to avoid unecessary
    #### complications at development environment. Since this script
    #### install Django using its correct version from the scratch, if
    #### it find Django in an older version, things should be tested...
    try:
        import django
    except ImportError:
        pass # It must already be present since we installed it previously (or it already exists).
    django_version = tuple()
    tmp = django.get_version().split('.')
    for i in tmp:
        django_version = django_version + (int(i),)
        
    if django_version < MINIMAL_DJANGO_VERSION:
        print("\n[Warning]    Missing Django (https://www.djangoproject.com)" \
              + str(MINIMAL_DJANGO_VERSION[0]) + "." \
              + str(MINIMAL_DJANGO_VERSION[1]) \
              + " (or greater) version.\n")
        print("Please, upgrade Django to a suitable version:\n")
        if env['system'] == 'Linux':
            print("Use\n\n    pip3 install django>=" \
                  + str(MINIMAL_DJANGO_VERSION[0]) + "." \
                  + str(MINIMAL_DJANGO_VERSION[1]) \
                  + "\nExiting.\n")
        if env['system'] == 'Windows':
            print("Use\n\n    pip.exe install django>=" \
                  + str(MINIMAL_DJANGO_VERSION[0]) + "." \
                  + str(MINIMAL_DJANGO_VERSION[1]) \
                  + "\nExiting.\n")
        sys.exit(1)

def cleaning_old_stuff():
    '''Cleaning projects old files into directory'''
    print("Cleaning old project structure...")
    target = Path(PROJECT_NAME)
    if target.is_dir():
        shutil.rmtree(target)
    
    print("Done.")

######## End of System properties.

######## Djngo properties:
def start_django_project():
    '''Builds the project.'''
    env = get_environment()
    print("Starting creating Django structure...")
    #### Starting project creation:
    os.system('django-admin startproject' + ' ' + PROJECT_NAME)
    os.chdir(PROJECT_NAME)

    #### Introducing APP_NAME into the project:
    if env['system'] == 'Linux':
        os.system('python3 manage.py startapp' + ' ' + APP_NAME)
    if env['system'] == 'Windows':
        os.system('python.exe manage.py startapp' + ' ' + APP_NAME)
    print("Done.")

def run():
    param = check_parameters()

    if param == "loadvenv":      
        load_venv()
        
    if param == "build":
        check_parameters()
        get_environment()
        load_venv()
        check_system_reqs()
        cleaning_old_stuff()
        start_django_project()
    
    if param == "clean":
        cleaning_old_stuff()
        
   
run()
