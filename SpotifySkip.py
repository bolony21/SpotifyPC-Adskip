import sys
import time
import os
import threading
import tkinter 
import psutil
import keyboard

filepath = 'Spotify.exe'

gui = tkinter.Tk()
 
myLabel1 = tkinter.Label(gui,text="    Program is Currently running, To skip an ad press the ] key, it will close and reopen spotify ")
myLabel2 = tkinter.Label(gui,text="   To stop the program press the = key ")
myLabel3 = tkinter.Label(gui,text=" (By bolony21 - Version 1.0) ")

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
myLabel3.grid(row=2,column=0)

gui.update()

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed(']'):
           for process in (process for process in psutil.process_iter() if process.name()=="Spotify.exe"):
              process.kill()
              time.sleep(3)
              os.startfile(filepath)
        if keyboard.is_pressed('='):
          sys.exit()
    except:
          break



