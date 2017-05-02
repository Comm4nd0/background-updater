# background-updater

#### This program updates your desktop backgound using images from /r/EarthPorn.

================================================================================
 *To install* 
 * git clone this repo.
 * go here: https://www.reddit.com/prefs/apps and create a new app.
 * get your client_id and client_secret and put them into the main code.
 * ensure the path to the folder where the main.py is running from is correct.
 * copy the background-changer.service to /etc/systemd/system/
 * run systemctl enable background-changer.service.
 * reboot and it should be working!