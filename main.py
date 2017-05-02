#!/usr/bin/python3

import os
import praw
import urllib.request
from random import randint
import time

img_ext = ('.jpg','.jpeg','.png','.bmp')
urls = []
sub = 'earthporn'

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
            res = os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri "file:///home/{USERNAME}/projects/background-changer/img"')
            time.sleep(60)
        else:
            continue

def get_urls(reddit):
    rand_num = randint(1, 20)
    del urls[:]
    for submission in reddit.subreddit(sub).hot(limit=rand_num):
        urls.append(submission.url)
    return rand_num
if __name__ == "__main__":
  main()z