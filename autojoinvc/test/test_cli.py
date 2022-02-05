import click

import test_config as conf

@click.command()
def list_all():
    conf.show_all_data()


@click.command()
@click.argument("subject")
def search(subject):
    conf.show_data(subject)


@click.command()
def status():
    conf.show_status()


@click.command()
def on():
    conf.change_status(True)


@click.command()
def off():
    conf.change_status(False)


@click.command()
def remove_all():
    conf.remove_all_data()


@click.command()
@click.argument("subject")
def remove(subject):
    conf.remove_data(subject)


@click.command()
@click.option("--status", metavar="on/off")
@click.option("--subj", required=True, metavar="subject")
@click.option("--day", required=True, type=int, metavar="day")
@click.option("--time", required=True, metavar="HH:MM:SS")
@click.option("--link", required=True, metavar="link")
def add(subj, day, time ,link, status):
    if status == "on":
        conf.add_data(subj, day ,time, link)
        conf.change_status(True)
    elif status == "off":
        conf.add_data(subj, day, time ,link)
        conf.change_status(False)
    else:
        conf.add_data(subj, day, time ,link)


if __name__ == "__main__":
    pass