#!/usr/bin/python3
# -*- coding: utf-8 -*-

import praw
import urllib.request
from random import randint
import time
import os
from configparser import ConfigParser
from bs4 import BeautifulSoup

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
            set_bg(url)
        elif "imgur" in url:
            r = urllib.request.urlopen(url)
            soup = BeautifulSoup(r, "lxml")
            res = soup.find_all(class_="zoom")
            for link in res:
                srcurl = link.get("href")
                srcurl = "http://" + srcurl[2:]
                set_bg(srcurl)
        else:
            continue

def set_bg(url):
    urllib.request.urlretrieve(url, "img")
    change_image_ubuntu = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri "file:'
    img_path = os.getcwd() + '/img"'
    command_combined = change_image_ubuntu + img_path
    os.system(command_combined)
    time.sleep(int(Config.get('settings', 'interval')))

def get_urls(reddit):
    rand_num = randint(1, int(Config.get('settings', 'sub_count')))
    del urls[:]
    subs = (Config.get('settings', 'sub'))
    indiv_subs = subs.split(',')

    sub_num = randint(0, len(indiv_subs)-2)

    for submission in reddit.subreddit(indiv_subs[sub_num]).hot(limit=rand_num):
        urls.append(submission.url)
    return rand_num

if __name__ == '__main__':
    main()
