from datetime import datetime
import json, time, psutil, os

filename = "config.json"
timeList = []

with open(filename) as mf:
    content = json.load(mf)
    content.pop("status")

for i in content.values():
    timeList.append(i["meeting_time"])

def current_time():
    return datetime.now().strftime("%H:%M:%S")

def zoom_status():
    return "zoom" in (i.name() for i in psutil.process_iter())

def zoom_kill():
    time.sleep(3)# meeting length
    if zoom_status() and current_time() > max(timeList):
        print("kill zoom end")
        os.system("pkill zoom")
        exit()
    elif zoom_status():
        print("kill zoom continue")
        os.system("pkill zoom")
        return
    else:
        return


def script_kill():
    if current_time() > max(timeList):
        print("exit")
        exit()
    else:
        return


if __name__ == "__main__":
    pass