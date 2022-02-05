import json

import test_setup as su

file1 = su.config_file_1
file2 = su.config_file_2

def show_all_data():
    with open(file1) as mf1, open(file2) as mf2:
        config = json.load(mf1)
        meetings = json.load(mf2)

    for k, v in config.items():
        if k == "status":
            if v:
                print("Status: On")
            elif v is False:
                print("Status: Off")
            else:
                print("Status: null")
            continue
        
        print(f"{k.title()}: {v}".replace("_", " "))

    for x, y in meetings.items():
        print(f" - {x.title()}: {y}".replace("_", " "))


def show_data(subject):
    with open(file2) as mf:
        meetings = json.load(mf)

    if subject in meetings:
        print(subject.title()) 
        for k, v in meetings[subject].items():
            print(f" - {k.title()}: {v}".replace("_", " "))
    else:
        print(f"{subject.title()} not found")


def show_status():
    with open(file1) as mf:
        config = json.load(mf)

    if config["status"]:
        return print("Status: On")
    elif config["status"] is False:
        return print("Status: Off")
    else:
        return print("Status: null")


def change_status(status):
    """CHANGES THE STATUS IN THE CONFIG FILE TO TRUE OR FALSE"""
    with open(file1) as mf:
        config = json.load(mf)
    
    config["status"] = status

    with open(file1, 'w') as mf:
        json.dump(config, mf)


def remove_all_data():
    """REMOVES ALL THE ENTRIES IN THE CONFIG FILE EXCEPT FOR THE STATUS KEY-VALUE PAIR"""
    with open(file1, 'w') as mf1, open(file2) as mf2:
        json.dump(su.config, mf1)
        json.dump(su.meetings, mf2)


def remove_data(subject):
    """REMOVES THE SPECIFIED SUBJECT IN THE CONFIG FILE"""
    with open(file2) as mf:
        meetings = json.load(mf)
    
    try:
        meetings.pop(subject)
    except KeyError:
        print(f"{subject.title()} not found")
    
    with open(file2, 'w') as mf:
        json.dump(meetings, mf)


def add_data(subject, day, time, link):
    """ADDS NEW DATA TO THE CONFIG FILE"""
    with open(file2) as mf:
        meetings = json.load(mf)

    meetings[subject] = {"day": day, "meeting_time": time, "meeting_link": link}

    with open(file2, 'w') as mf:
        json.dump(meetings, mf)


if __name__ == "__main__":
    pass