#!/usr/bin/python3
# -*- coding: utf-8 -*-

import praw
import urllib.request
from random import randint, choice
import time
import os
from configparser import ConfigParser
from bs4 import BeautifulSoup

img_ext = ('.jpg','.jpeg','.png','.bmp')

config = ConfigParser()
config.read("settings.cfg")
SUBS = config['settings']['sub'].split(',')
SUB_COUNT = int(config['settings']['sub_count'])
INTERVAL = int(config['settings']['interval'])

def main():
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         user_agent='reddit scraper')
    while True:
        url = get_url(reddit)
        if is_image(url):
            set_bg(url)
        elif "imgur" in url:
            r = urllib.request.urlopen(url)
            soup = BeautifulSoup(r, "lxml")
            res = soup.find_all(class_="zoom")
            for link in res:
                srcurl = link.get("href")
                srcurl = "http://" + srcurl[2:]
                set_bg(srcurl)

def set_bg(url):
    urllib.request.urlretrieve(url, "img")
    change_image_ubuntu = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri "file:'
    img_path = os.getcwd() + '/img"'
    command_combined = change_image_ubuntu + img_path
    os.system(command_combined)
    time.sleep(INTERVAL)

def get_url(reddit):
    submissions = reddit.subreddit(choice(SUBS)).hot(limit=randint(1, SUB_COUNT))
    for last_submission in submissions:
        pass
    return last_submission.url

def is_image(url):
    return os.path.splitext(url)[1] in ('.jpg','.jpeg','.png','.bmp')

if __name__ == '__main__':
    main()
