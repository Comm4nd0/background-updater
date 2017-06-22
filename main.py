#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import subprocess
import configparser
from tkinter.scrolledtext import ScrolledText

subporn = ('AbandonedPorn', 'AdPorn', 'AdrenalinePorn', 'AerialPorn', 'AgriculturePorn', 'AlbumArtPorn', 'AnimalPorn',\
          'ApocalypsePorn', 'ArchitecturePorn', 'ArtefactPorn', 'ArtPorn', 'AutumnPorn', 'avporn', 'Beachporn',\
        'boatporn', 'BonsaiPorn', 'bookporn', 'BotanicalPorn', 'bridgeporn', 'CabinPorn', 'carporn', 'CemeteryPorn',\
        'churchporn', 'CityPorn', 'ClimbingPorn', 'ComicBookPorn', 'CulinaryPorn', 'desertporn', 'DesignPorn', \
        'dessertPorn', 'DestructionPorn', 'drydockporn', 'EarthlingPorn', 'EarthPorn', 'ExposurePorn', 'F1Porn',\
        'fashionporn', 'FirePorn', 'FoodPorn', 'FossilPorn', 'FractalPorn', 'futureporn', 'GamerPorn', 'GeekPorn',\
        'geologyporn', 'GunPorn', 'HellscapePorn', 'HistoryPorn', 'Houseporn', 'HumanPorn', 'InfraredPorn',\
        'InfrastructurePorn', 'InstrumentPorn', 'Knifeporn', 'lakeporn', 'lavaporn', 'MachinePorn', 'MacroPorn',\
        'MapPorn', 'MegalithPorn', 'MetalPorn', 'MicroPorn', 'MilitaryPorn', 'MotorcyclePorn', 'MoviePosterPorn',\
        'mtgporn', 'MushroomPorn', 'NewsPorn', 'OrganizationPorn', 'policeporn', 'powerwashingporn', 'QuotesPorn',\
        'retailporn', 'RetroGamePorn', 'RidesPorn', 'RoomPorn', 'ruralporn', 'seaporn', 'SkyPorn', 'spaceflightporn',\
        'spaceporn', 'SportsPorn', 'SpringPorn', 'stadiumporn', 'StarshipPorn', 'steamporn', 'StreetArtPorn',\
        'SummerPorn', 'TeaPorn', 'TechnologyPorn', 'TelevisionPosterPorn', 'ThingsCutInHalfPorn', 'toolporn',\
        'uniformporn', 'VideoPorn', 'ViewPorn', 'VillagePorn', 'waterporn', 'WeatherPorn', 'winterporn')

img_ext = ('.jpg','.jpeg','.png','.bmp')
urls = []
Config = configparser.ConfigParser()
Config.read("settings.cfg")
SUBS = []
B = True
C = tk.Checkbutton

class Choices(ScrolledText):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, cursor="arrow", **kwargs)
        for sub in subporn:
            B = tk.BooleanVar(master)
            C = tk.Checkbutton(self, text=sub, variable=B, bg='black', fg='white', selectcolor='#111', borderwidth=3, highlightthickness=0)
            self.window_create(tk.END, window=C,)
            self.insert(tk.END, '\n')
            SUBS.append((sub, C, B))
        self.config(state=tk.DISABLED, bg=C['bg'], width=25, height=15, background='black')

class GUI(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.center(400, 500)
        self.master.configure(background='black')
        self.master.title("Desktop Background Changer")

        # causes the full width of the window to be used
        self.columnconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)
        self.make_UI()

    def make_UI(self):
        style = ttk.Style()
        # global style changes
        style.configure(".", background='black', foreground='grey', anchor="center")
        # Button style changes
        style.map("TButton", background=[('hover', 'blue')])

        style.map("TMenubutton", background=[('hover', 'blue')])
        style.map("TEntry", foreground=[('focus', 'blue2')])
        style.map("TEntry", foreground=[('active', 'green2')])

        heading = ttk.Label(self, text="Desktop Background", font=("Courier", 20))
        heading.grid(column=0, row=1, rowspan=1, columnspan=2, sticky='NWES')

        heading = ttk.Label(self, text="Changer", font=("Courier", 20))
        heading.grid(column=0, row=2, rowspan=1, columnspan=2, sticky='NWES')

        intro = ttk.Label(self, font=("Courier", 16))
        intro['text'] = "Welcome to the DBC! "
        intro.grid(column=0, row=3, rowspan=2, columnspan=2, sticky='NWES', padx=5, pady=20)

        sub_text = ttk.Label(self, font=("Courier", 12))
        sub_text['text'] = "Choose subs"
        sub_text.grid(column=0, row=6, sticky='E', padx=5, pady=5)

        # scroll area with multi selection
        c = Choices(self, width=30, height=10)
        c.grid(column=1, row=6, sticky='W', padx=5, pady=5)

        interval_text = ttk.Label(self, font=("Courier", 12))
        interval_text['text'] = "Interval(time)"
        interval_text.grid(column=0, row=7, sticky='E', padx=5, pady=5)

        self.interval = ttk.Entry(self)
        current_sub = Config.get('settings', 'interval')
        self.interval.insert(0, current_sub)
        self.interval.grid(column=1, row=7, sticky='W', padx=5, pady=5)

        sub_count_text = ttk.Label(self, font=("Courier", 12))
        sub_count_text['text'] = "Post Count"
        sub_count_text.grid(column=0, row=8, sticky='E', padx=5, pady=5)

        self.sub_count = ttk.Entry(self)
        sub_count = Config.get('settings', 'sub_count')
        self.sub_count.insert(0, sub_count)
        self.sub_count.grid(column=1, row=8, sticky='W', padx=5, pady=5)

        # EXIT
        exit_button = ttk.Button(self, text="Exit", command=self.exit)
        exit_button.grid(column=0, row=9, sticky='N')

        update_button = ttk.Button(self, text="Update", command=self.install)
        update_button.grid(column=1, row=9, sticky='N')

    def center(self, width, height):
        """center the window on the screen"""
        # get screen width and height
        ws = self.master.winfo_screenwidth()  # width of the screen
        hs = self.master.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def exit(self):
        quit()

    def install(self):
        config = configparser.RawConfigParser()
        sub = [sub for sub, C, B in SUBS if B.get()]
        time = self.interval.get()
        count = self.sub_count.get()
        subs = ''
        config.add_section('settings')
        for res in sub:
            subs += res + ','
        config.set('settings', 'sub', subs)
        config.set('settings', 'interval', time)
        config.set('settings', 'sub_count', count)

        with open('settings.cfg', 'w') as configfile:
            config.write(configfile)

        subprocess.Popen('./install.sh')

if __name__ == '__main__':
    root = tk.Tk()
    window = GUI(root)
    window.pack(fill=tk.X, expand=True, anchor=tk.N)
    root.mainloop()