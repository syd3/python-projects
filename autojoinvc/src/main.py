#!/usr/bin/env python3

import webbrowser as wb
import pyautogui as pyg
import json
import time
import click
import sys

import cli as cl
import extras as ext
import setup as su

with open(su.config_file_1) as mf1, open(su.config_file_2) as mf2:
    config = json.load(mf1)
    meetings = json.load(mf2)

def meeting_link():
    """
    Reads from the json file and checks certain conditions which if met, will
    return the meeting link for the zoom meeting
    """
    while True:
        time.sleep(1)
        for subj in meetings.values():
            if ext.current_day == subj["day"]:
                if ext.current_time() == subj["meeting_time"]:
                    return subj["meeting_link"]


def join_meeting():
    """
    Opens a zoom meeting link from the meeting_link function using firefox and
    uses the img_path key (which is the png file from the buttons dir) from 
    the config file to determine where to click. Will loop 10 times until the
    open link prompt pops up and clicks on it and then calls the zoom_kill function
    from the extras module
    """
    wb.get(using="firefox").open(meeting_link(), new=2)
    for i in range(20):
        try:
            pyg.click(x=config["img_path"])
        except:
            if FileNotFoundError:
                time.sleep(1)
                continue
        else:
            ext.zoom_kill()
            join_meeting()


def main():
    """
    The function in which the run command executes. Will execute the join_meeting 
    function but first checks for the status. If status is False, script will not
    run. If its null or detects that other required config are missing, script 
    will not run.

    Script will then check if there's any meetings that will occur on the day it
    is executed, if there is, script continues. Otherwise, script will exit
    """
    if config["status"] is False:
        sys.exit()
    elif config["status"] is not None and len(meetings) == 0:
        print("No meeting configurations detected")
        print("Please configure links and meeting times first")
        sys.exit()
    elif config["status"] is None:
        print("Status is null. Set it to on/off. See --help for more info")
        sys.exit()
    elif config["status"] is None and len(meetings) == 0:
        print("Status is null and no meeting configurations detected")
        print("Please configure links and meeting times first")
        sys.exit()

    for subj in meetings.values():
        if ext.current_day == subj["day"]:
            ext.script_kill()
            join_meeting()
    else:
        sys.exit()


@click.group()
def cli():
    pass

@cli.command()
def run():
    """runs the script"""
    main()

cmds = [cl.list_all, cl.search, cl.status, cl.on, cl.off,
    cl.remove_all, cl.remove, cl.add]
# initializes the commands for the cli interface
for i in cmds:
    cli.add_command(i)

if __name__ == "__main__":
    cli()