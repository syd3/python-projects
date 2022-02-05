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
2. Add the main.py script from src to PATH or make a symbolic link to a directory included in the PATH like /usr/local/bin and make it executable using chmod.
3. Run the script either by typing main.py or whatever you named the file on your terminal (if it was added to your PATH) or by running it directly from the repo by typing `python3 main.py`
4. Enter the proper configuration (png file path and meeting length). The png the script is referring to is the open_link.png file in the buttons dir. It can be found in this repo. Just add the absolute path to that file. And the meeting length should be in minutes. Example, if the meeting is 2 hours, input should be 120, 1 hr = 60 minutes, 2 hrs = 120 minutes.
5. Add your subject configurations by doing:
```
autojoinvc add --subj <subject name here> --time <time here> --day <day here> --link <link here> --status <on/off>
```
The --time option uses military time format. And the --day option refers to a day in the weekday or weekend, and are represented as integers. See additional notes below for more info.

6. Add this command to your startup applications:
`main.py run`
The "run" command is an option in the script. Without it, the script will not run and will instead throw the --help prompt.

7. Wait for the meeting time for the script to execute. Restart your system if the meeting is going to occur the same day you configured this script. (For the script to be executed at startup)

For more options, use the --help option to see the available commands.

## Additional notes

The requirements.txt file contains all the dependencies needed in order to run the code in the src dir. However, it's not needed to install the dependencies if you're not gonna change anything in the src code.

In the script config, when adding subjects. Days are represented as integers. Mon - 0, Tues - 1, Wed - 2, Thurs - 3, Fri - 4, Sat - 5, Sun - 6

In order for the script to execute properly, you first must install `python3-tk` & `python3-dev`. You can do so by running the below command:
`sudo apt install python3-tk python3-dev`