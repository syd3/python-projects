#!/usr/bin/env python3

import os
import sys
import json
import imghdr

home = os.environ["HOME"] # stores the home environment variable of the OS
config_dir = f"{home}/.autojoinvc"
config_file_1 = f"{config_dir}/config.json"
config_file_2 = f"{config_dir}/meetings.json"
default_config = {"status": None, "img_path": "", "meeting_length": None}
default_meetings = {}

def file_path():
    """
    Takes in a file path as input and verifies if its a png file. If it is,
    the path gets written to the json file. Otherwise, script will throw an error.
    """
    prompt = "Enter the absolute path of the open_link.png file:\n> "
    user_input = input(prompt)

    if os.path.isfile(user_input) is True and imghdr.what(user_input) == "png":
        with open(config_file_1) as mf:
            config = json.load(mf)

        config["img_path"] = user_input

        with open(config_file_1, "w") as mf:
            json.dump(config, mf)
    else:
        error = "File not found\nPlease run the setup again with the"
        error += " correct path"
        raise FileNotFoundError(error)


def meeting_length():
    """
    Takes in the meeting length as an integer and converts it from minutes to
    seconds. Which will then write the input to the json file.
    """
    prompt = "Enter meeting length in minutes. Example:\n"
    prompt += "If the meeting is 1 hr and 30 minutes, input should be 90\n> "

    with open(config_file_1) as mf:
        config = json.load(mf)

    try:
        user_input = int(input(prompt))
    except ValueError:
        print("Not a number. Please enter the correct data type")
    else:
        user_input = (user_input * 60) - 300
        config["meeting_length"] = user_input

        with open(config_file_1, "w") as mf:
            json.dump(config, mf)

        sys.exit()


def setup():
    """
    Function first checks if the required directory and files are already in the
    system, if it is, it checks if it has the required files and configurations.
    Otherwise, it'll make the directory and files and prompt the user for the
    required configuration
    """
    if os.path.exists(config_dir) is True:
        try:
            with open(config_file_1) as mf:
                config = json.load(mf)
        except FileNotFoundError:
            with open(config_file_1, "w") as mf:
                json.dump(default_config, mf)
            
            file_path()
            meeting_length()
        else:
            if len(config["img_path"]) == 0:
                file_path()
            if config["meeting_length"] is None:
                meeting_length()
        finally:
            if os.path.exists(config_file_2) is False:
                with open(config_file_2, "w") as mf:
                    json.dump(default_meetings, mf)     
    else:
        os.mkdir(f"{config_dir}", mode=0o700)

        with open(config_file_1, "w") as mf1, open(config_file_2, "w") as mf2:
            json.dump(default_config, mf1)
            json.dump(default_meetings, mf2)

        file_path()
        meeting_length()


if __name__ == "__main__":
    pass