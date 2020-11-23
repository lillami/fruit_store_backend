#!/usr/bin/env python3

'''
(...) The script should check the system statistics every 60 seconds, and in event of any issues detected among the ones
mentioned above, an email should be sent with the following content:

CPU usage is over 80% : Error - CPU usage is over 80%
Available disk space is lower than 20% : Error - Available disk space is less than 20%
available memory is less than 500MB : Error - Available memory is less than 500MB
hostname "localhost" cannot be resolved to "127.0.0.1" : Error - localhost cannot be resolved to 127.0.0.1
'''

import shutil, psutil
import os, sys
import emails

#doing health checks
def high_CPU_usage():
    if psutil.cpu_percent(>80):
        return True

def low_disk_space("/"):
    usage = shutil.disk_usage(os.getcwd())
    THRESHOLD = usage.free / usage.total * 100 # %
    if THRESHOLD < 20: #20%
        return True

def low_memory():
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024  # 500MB
    if mem.available <= THRESHOLD:
        return True

def localhost_check():
    hostname = "127.0.0.1"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return True

def sendErrorEmail(subject):
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email('automation@example.com', "{}@example.com".format(os.environ["USER"]), subject, body)
    emails.send_email(message)

#subject line
def main(argv):
    if high_CPU_usage():
        sendErrorEmail("Error - CPU usage is over 80%")
    if low_disk_space():
        sendErrorEmail("Error - Available disk space is less than 20%")
    if low_memory():
        sendErrorEmail("Error - Available memory is less than 500MB")
    if not localhost_check():
        sendErrorEmail("Error - localhost cannot be resolved to 127.0.0.1")


if __name__ == "__main__":
    main(sys.argv)
