from datetime import datetime
import webbrowser as wb
import pyautogui as pyg
import json, time, click

import test_cli as cl
import test_extras as ext
import test_setup as su

curent_day = datetime.today().weekday()

try:
    with open(su.config_file_1) as mf1, open(su.config_file_2) as mf2:
        config = json.load(mf1)
        meetings = json.load(mf2)
except FileNotFoundError:
    su.setup()

    print("\nPlease set up meeting links and meeting times. See --help for more info")
    exit()

def meeting_link():
    while True:
        time.sleep(1)
        for i in meetings.values():
            if curent_day == i["day"]:
                print(f"running - {ext.current_time()}")
                if ext.current_time() == i["meeting_time"]:
                    return i["meeting_link"]


def join_meeting():
    wb.get(using='firefox').open(meeting_link(), new=2)
    for i in range(10):
        try:
            pyg.click(x="../buttons/open_link.png")
        except:
            if FileNotFoundError:
                print("except continue")
                continue
            #else:
                # for handling other types of errors?? if any
        else:
            ext.zoom_kill()
            join_meeting()
    #else:
        # add a failsafe incase the code above wasnt able to locate the img


def main():
    if config["status"] is False:
        exit()
    elif config["status"] is None and len(meetings) > 0:
        print("Status is null. Set it to on/off. See --help for more info")
        exit()
    elif config["status"] is None and len(meetings) == 0:
        print("Status is null. And no meeting configurations detected")
        print("Please configure meeting links and meeting times first")
        exit()

    for n in meetings.values():
        if curent_day == n["day"]:
            ext.script_kill()
            join_meeting()
    else:
        exit()


@click.group()
def cli():
    pass

@cli.command()
def run():
    main()

cmds = [cl.list_all, cl.search, cl.status, cl.on, cl.off, 
        cl.remove_all, cl.remove, cl.add]

for i in cmds:
    cli.add_command(i)

if __name__ == "__main__":
    cli()