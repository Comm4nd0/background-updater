#!/usr/bin/python3
# -*- coding: utf-8 -*-

import praw
import urllib.request
from random import randint
import time
import os
from configparser import ConfigParser

img_ext = ('.jpg','.jpeg','.png','.bmp')
urls = []

Config = ConfigParser()
Config.read("settings.cfg")

def main():
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         user_agent='reddit scraper')
    while True:
        rand_num = get_urls(reddit)
        url = urls[rand_num-1]
        filename, file_extension = os.path.splitext(url)
        if file_extension in img_ext:
            urllib.request.urlretrieve(url, "img")
            change_image_ubuntu = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri "file:'
            img_path = os.getcwd() + '/img"'
            command_combined = change_image_ubuntu + img_path
            os.system(command_combined)
            time.sleep(int(Config.get('settings', 'interval')))
        else:
            continue

def get_urls(reddit):
    rand_num = randint(1, int(Config.get('settings', 'sub_count')))
    del urls[:]
    for submission in reddit.subreddit(Config.get('settings', 'sub')).hot(limit=rand_num):
        urls.append(submission.url)
    return rand_num

if __name__ == '__main__':
    main()
