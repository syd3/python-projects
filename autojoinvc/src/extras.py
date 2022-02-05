#!/usr/bin/env python3

from datetime import datetime as dt
import json
import time
import psutil
import os
import sys

import setup as su

current_day = dt.today().weekday() # stores the current day using int from 0-6
time_list = []

with open(su.config_file_1) as mf1, open(su.config_file_2) as mf2:
    config = json.load(mf1)
    meetings = json.load(mf2)

for subj in meetings.values(): # appends all the meeting times for the current day-
    if current_day == subj["day"]: # to a list for later use
        time_list.append(subj["meeting_time"])

def current_time():
    """Returns the current time in military time format"""
    return dt.now().strftime("%H:%M:%S")

def zoom_status():
    """Checks if the zoom process is running"""
    return "zoom" in (i.name() for i in psutil.process_iter())

def zoom_kill():
    """
    Kills the zoom app based on certain conditions, or returns to the main
    script if no other condition was met
    """
    time.sleep(config["meeting_length"])
    if zoom_status() is True and current_time() > max(time_list):
        os.system("pkill zoom")
        sys.exit()
    elif zoom_status() is True:
        os.system("pkill zoom")
    #    return
    #else:
    #    return


def script_kill():
    """
    Kills the script if it detects that its past the latest meeting time, will
    return if otherwise
    """
    if current_time() > max(time_list):
        sys.exit()
    #else:
    #    return


if __name__ == "__main__":
    pass