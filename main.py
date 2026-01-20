'''
    This is script file for scripting week project

    Simulation ...

    It’s 10:30 AM on a Tuesday. A high-priority ticket hits the queue: "Customer 8821 cannot checkout.
    Getting a generic Error 500." Normally, the Support Engineer would spend the next 20 minutes:

    -Opening a terminal to check which version of the app is currently live.
    -Logging into a PostgreSQL client to see if Customer 8821’s account is locked or has a weird status.
    -SSH-ing into the application server to grep for "Error 500" in a 2GB log file.
    -Manually creating the issue report to IT platforms

'''

import sys
import  requests as rq

if sys.argv[1]=="--userid":

    try:
        userid = sys.argv[2]

        # read app's status (endpoint)
        # check the current status of the application to make sure if the problem is app side
        # or end user issue

        appdata = rq.get("http://127.0.0.1:8000/api/health")
        print(appdata.json()["status"])


        # read app log
        logdata = open(r"\\wsl.localhost\Ubuntu\home\\albert\coolmeapp\app-log.txt","r")
        for line in logdata:
            if "User "+userid in line:
                print(line)

        # read app's database



    except IndexError:
        print("Usage: python main.py --userid <userid>")




