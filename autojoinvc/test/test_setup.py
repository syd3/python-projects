import os, json

home = os.environ["HOME"]
config_dir = f"{home}/.autojoinvc"

config_file_1 = f"{config_dir}/config.json"
config_file_2 = f"{config_dir}/meetings.json"

config = {"status": None, "img_path": "", "meeting_length": ""}
meetings = {}

def img_path():
    img_prompt = "Please enter the absolute path of the open_link.png file:\n"
    img_prompt += "> "

    img_input = input(img_prompt)

    if os.path.isfile(img_input):
        with open(config_file_1) as mf:
            content = json.load(mf)

        content["img_path"] = img_input

        with open(config_file_1, "w") as mf:
            json.dump(content, mf)
    else:
        error_prompt = "File not found. Perhaps theres a typo\n"
        error_prompt += "Please run the setup again with the correct path"
        raise FileNotFoundError(error_prompt)


def ml_time():
    ml_prompt = "Please enter meeting length prompt in minutes. Example: "
    ml_prompt += "If the meeting is 1 hr and 30 mins, input should be 90\n"
    ml_prompt += "> "

    with open(config_file_1) as mf:
        content = json.load(mf)

    try:
        ml_input = int(input(ml_prompt))
    except ValueError:
        print("Not a number. Please enter the correct data type")
    else:
        ml_input = (ml_input * 60) - 300
        content["meeting_length"] = ml_input

        with open(config_file_1, "w") as mf:
            json.dump(content, mf)


def setup():
    if os.path.exists(config_dir):
        try:
            with open(config_file_1) as mf:
                content = json.load(mf)
        except FileNotFoundError:
            with open(config_file_1, "w") as mf:
                json.dump(config, mf)

            img_path()
            ml_time()
        else:
            if len(content["img_path"]) == 0:
                img_path()
            if len(content["meeting_length"]) == 0:
                ml_time()
        finally:
            if os.path.exists(config_file_2) is False:
                with open(config_file_2, "w") as mf:
                    json.dump(meetings, mf)
    else:
        os.mkdir(f"{config_dir}", mode=0o700)

        with open(config_file_1, "w") as mf1, open(config_file_2, "w") as mf2:
            json.dump(config, mf1)
            json.dump(meetings, mf2)

        img_path()
        ml_time()

if __name__ == "__main__":
    setup()