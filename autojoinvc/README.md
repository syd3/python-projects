# autojoinvc v2

A python script that will automatically join zoom meeting for you based on the configurations you give.

This script is primarily for joining zoom meeting classes. Not meetings that are going to occur just once.

## What it does

1. Automatically joins zoom meetings.
2. Joins meetings by opening the zoom meeting link directly from the browser.
3. Uses json files to save configurations.
4. Kills the zoom process after the given meeting length which is a fixed time.
5. Script stops after the latest meeting, as well as if there's no meeting that's gonna occur when it's executed based on the config.

## Prerequisites

1. Zoom must be installed.
2. Script assumes that you're using firefox as your browser.
3. Script also assumes that when you're opening zoom links, it directly leads to the open link prompt, not any other prompt.
4. Must be on linux. This hasn't been tested on a windows environment nor was made with the intent of using it on a windows environment.
5. Must be quite familiar with the terminal in order to add the proper configuration as well as for further changes.
6. Script was also made with the intent of automatically starting it in startup applications

## How to use

1. Clone the repo.
2. Install the dependencies via `sudo apt install python3-tk python3-dev && pip install -r requirements.txt`
3. Navigate to the src/ directory and make main.py executable via `chmod +x main.py`.
4. Navigate to /usr/local/bin and make a symbolic link via `ln -s /path/to/repo/main.py autojoinvc`
5. Run the script by typing in `autojoinvc` in the terminal or by directly executing it from the src folder by entering `python3 main.py` or `./main.py` in the terminal.
6. Enter the proper configurations which are the open_link.png file path and the meeting length. The open_link.png file is located in the buttons/ folder, you can also locate it by using the `locate` command via `locate open_link.png`. And the meeting length is the average meeting length of all your zoom meetings and must be entered in minutes. Example, 1 hr == 60, 1 hr 30 mins == 90, 2 hrs == 120.
7. Add meeting configurations by using the syntax below:
```
autojoinvc add --subj <subject name> --time <meeting time> --day <day 0-6> --link <meeting link>
```
The `--time` option uses military time format. And the `--day` option refers to a day in the week, and are represented as integers from 0 (monday) through 6 (sunday).

Example meeting configuration that will occur on Monday at 12:00 PM:
```
autojoinvc add --subj Math --time 12:00:00 --day 0 --link https://<zoom link>.com
```

8. Turn the script on/off by `autojoinvc on` or `autojoinvc off`.
9. Add `autojoinvc run` command to the startup applications. The `run` option tells the script that you want to execute its main functionality, without it, it'll throw the --help prompt.
10. Wait until the day of the meeting. Restart your computer if the meeting is going to occur the same day you configured this script.

For more options, use the --help option to see the available commands.

## Additional notes

When adding subjects. Days are represented as integers. Mon - 0, Tues - 1, Wed - 2, Thurs - 3, Fri - 4, Sat - 5, Sun - 6