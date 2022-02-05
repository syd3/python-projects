#!/usr/bin/env python3

import json

import setup as su

file_1 = su.config_file_1
file_2 = su.config_file_2

try:
    with open(file_1) as mf1, open(file_2) as mf2:
        config = json.load(mf1)
        meetings = json.load(mf2)
except FileNotFoundError:
    print("No config files found. Making one now")
    print("Please set up meeting links and meeting times\n")
    print("See --help for more info")
    su.setup()
else: # checks the entries in the config file, prompts to setup if there's none
    if len(config["img_path"]) == 0 or config["meeting_length"] is None:
        su.setup()

def show_all_data():
    """Lists all the configurations of the user"""
    show_status()

    img_prompt = config["img_path"]
    print(f"Png File Path: {img_prompt}")

    ml_prompt = config["meeting_length"]
    ml_prompt /= 60
    print(f"Meeting Length: {ml_prompt} minute(s)")

    for x, y in meetings.items():
        print(f"\n{x.title()}:")
        for n, i in y.items():
            if n == "meeting_link":
                print(f" - Meeting Link: {i}")
                continue

            print(f" - {n.title()}: {i}".replace("_", " "))


def show_data(subject):
    """Shows the configuration of the specified subject"""
    if subject in meetings.keys():
        print(subject.title())
        for k, v in meetings[subject].items():
            print(f" - {k.title()}: {v}".replace("_", " "))
    else:
        print(f"{subject.title()} not found")


def show_status():
    """
    Shows the status of the script. On/Off/null. This is where the script checks
    whether to continue execution or not whenever the run command is used
    """
    if config["status"] is True:
        print("Status: On")
    elif config["status"] is False:
        print("Status: Off")
    else:
        print("Status: null")


def change_status(status):
    """Changes the status of the script to True/False"""
    config["status"] = status

    with open(file_1, "w") as mf:
        json.dump(config, mf)


def remove_all_data():
    """Removes all user config"""
    with open(file_1, 'w') as mf1, open(file_2, 'w') as mf2:
        json.dump(su.default_config, mf1)
        json.dump(su.default_meetings, mf2)


def remove_data(subject):
    """Removes only the config of the specified subject"""
    if subject in meetings.keys():
        meetings.pop(subject)

        with open(file_2, 'w') as mf:
            json.dump(meetings, mf)
    else:
        print(f"{subject.title()} not found")


def add_data(subject, day, time, link):
    """Adds meeting configuration if the subject is not already in the config file"""
    if subject not in meetings.keys():
        meetings[subject] = {
            "day": day, 
            "meeting_time": time, 
            "meeting_link": link,
            }

        with open(file_2, 'w') as mf:
            json.dump(meetings, mf)
    else:
        print("Subject is already in the config file")


if __name__ == "__main__":
    pass