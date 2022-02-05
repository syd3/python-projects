#!/usr/bin/env python3

import click

import config as conf

@click.command()
def list_all():
    """lists all the configurations"""
    conf.show_all_data()

@click.command()
@click.argument("subject")
def search(subject):
    """lists the config of the specified subject"""
    conf.show_data(subject)

@click.command()
def status():
    """shows the status of the script"""
    conf.show_status()

@click.command()
def on():
    """sets the status of the script to on/true"""
    conf.change_status(True)

@click.command()
def off():
    """sets the status of the script to off/false"""
    conf.change_status(False)

@click.command()
def remove_all():
    """removes all the configurations"""
    conf.remove_all_data()

@click.command()
@click.argument("subject")
def remove(subject):
    """removes the config of the specified subject"""
    conf.remove_data(subject)

@click.command()
@click.option("--status", 
        metavar="on/off", 
        help="sets the status of the script to on/off")
@click.option("--subj", 
        required=True, 
        metavar="subject",
        help="the name of the subject")
@click.option("--day", 
        required=True, 
        type=int, 
        metavar="day",
        help="the day of the week of the meeting, mon-sun is represented as 0-6")
@click.option("--time", 
        required=True, 
        metavar="hh:mm:ss",
        help="the time of the meeting, uses military time format")
@click.option("--link", 
        required=True, 
        metavar="link",
        help="the link for the zoom meeting")
def add(subj, day, time ,link, status):
    """adds new meeting config"""
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