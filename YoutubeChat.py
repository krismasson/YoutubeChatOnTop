from tkinter import *
import time
import win32gui
import win32api
import pytchat
from datetime import datetime
import pyttsx3

from win32api import GetSystemMetrics
# WIDTH = 500
# HEIGHT = 500

#Youtube Chat On Top Aggregator
#reads Youtube chat from address with the chat variable below
#places the chat on top of all programs
#I suppose the purpose would be for streamers who dont wanna use multiple monitors
#or just dont have multiple montiors,
#or would just rather have the chat real close by during the stream, no have to look over


chat = pytchat.create(video_id="GrvXQ3sEre0")
WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)
LINEWIDTH = 1
DELAY = 60
TRANSCOLOUR = 'gray'
title = 'Virtual whiteboard'
global old
old = ()
global HWND_t
HWND_t = 0

tk = Tk()
# tk.title(title)
tk.lift()
tk.wm_attributes("-topmost", True)
tk.wm_attributes("-transparentcolor", TRANSCOLOUR)
tk.attributes('-fullscreen', True)


state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack()
canvas.config(cursor='tcross')
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR, outline=TRANSCOLOUR)
id6 = canvas.create_text(5,600,fill="white",anchor=SW,font="Arial 18", text="")
id5 = canvas.create_text(5,625,fill="white",anchor=SW,font="Arial 18", text="")
id4 = canvas.create_text(5,650,fill="white",anchor=SW,font="Arial 18", text="")
id3 = canvas.create_text(5,675,fill="white",anchor=SW,font="Arial 18", text="")
id2 = canvas.create_text(5,700,fill="white",anchor=SW,font="Arial 18", text="")
id1 = canvas.create_text(5,725,fill="white",anchor=SW,font="Arial 18", text="")


engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
#above is for voice stuff.


#COMMENTS? more like, someone help me learn to use arrays or something
#maybe its okay. initilize 6 spots. 
#the next function rotates them.

def nextline(date,name,msg):
    canvas.itemconfigure(id6, text=canvas.itemcget(id5, 'text'))
    canvas.itemconfigure(id5, text=canvas.itemcget(id4, 'text'))
    canvas.itemconfigure(id4, text=canvas.itemcget(id3, 'text'))
    canvas.itemconfigure(id3, text=canvas.itemcget(id2, 'text'))
    canvas.itemconfigure(id2, text=canvas.itemcget(id1, 'text'))
    newdate = date.split(" ")
    newdate2 = newdate[1]
    canvas.itemconfigure(id1, text=f"{newdate2} {name}: {msg}")
    engine.say(f"{msg}")
    engine.runAndWait()
#this function below checks for old comments removes them if their life goes past the DELAY
#it executes like a million times a second so it probably needs to be fixed xD
def checkforoldies():
    mint = len( canvas.itemcget(id6, 'text') )
    if (mint > 0):
        createtime = canvas.itemcget(id6, 'text').split(" ")
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        now = datetime.strptime(now, "%H:%M:%S")
        then = datetime.strptime(createtime[0], "%H:%M:%S")
        delta = now - then
        if (delta.total_seconds() > DELAY):
            canvas.itemconfigure(id6, text="")
    mint = len( canvas.itemcget(id5, 'text') )
    if (mint > 0):
        createtime = canvas.itemcget(id5, 'text').split(" ")
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        now = datetime.strptime(now, "%H:%M:%S")
        then = datetime.strptime(createtime[0], "%H:%M:%S")
        delta = now - then
        if (delta.total_seconds() > DELAY):
            canvas.itemconfigure(id5, text="")
    mint = len( canvas.itemcget(id4, 'text') )
    if (mint > 0):
        createtime = canvas.itemcget(id4, 'text').split(" ")
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        now = datetime.strptime(now, "%H:%M:%S")
        then = datetime.strptime(createtime[0], "%H:%M:%S")
        delta = now - then
        if (delta.total_seconds() > DELAY):
            canvas.itemconfigure(id4, text="")
    mint = len( canvas.itemcget(id3, 'text') )
    if (mint > 0):
        createtime = canvas.itemcget(id3, 'text').split(" ")
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        now = datetime.strptime(now, "%H:%M:%S")
        then = datetime.strptime(createtime[0], "%H:%M:%S")
        delta = now - then
        if (delta.total_seconds() > DELAY):
            canvas.itemconfigure(id3, text="")
    mint = len( canvas.itemcget(id2, 'text') )
    if (mint > 0):
        createtime = canvas.itemcget(id2, 'text').split(" ")
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        now = datetime.strptime(now, "%H:%M:%S")
        then = datetime.strptime(createtime[0], "%H:%M:%S")
        delta = now - then
        if (delta.total_seconds() > DELAY):
            canvas.itemconfigure(id2, text="")
    mint = len( canvas.itemcget(id1, 'text') )
    if (mint > 0):
        createtime = canvas.itemcget(id1, 'text').split(" ")
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        now = datetime.strptime(now, "%H:%M:%S")
        then = datetime.strptime(createtime[0], "%H:%M:%S")
        delta = now - then
        if (delta.total_seconds() > DELAY):
            canvas.itemconfigure(id1, text="")
def putOnTop(event):
    event.widget.unbind('<Visibility>')
    event.widget.update()
    event.widget.lift()
    event.widget.bind('<Visibility>', putOnTop)
def drawline(data):
    global old
    if old !=():
        canvas.create_line(old[0], old[1], data[0], data[1], width=LINEWIDTH)
    old = (data[0], data[1])

def enumHandler(hwnd, lParam):
    global HWND_t
    if win32gui.IsWindowVisible(hwnd):
        if title in win32gui.GetWindowText(hwnd):
            HWND_t = hwnd




win32gui.EnumWindows(enumHandler, None)

tk.bind('<Visibility>', putOnTop)
tk.focus()


running = 1
while running == 1:
    try:
        tk.update()
        time.sleep(0.01)
        checkforoldies()
        for c in chat.get().sync_items():
            nextline(c.datetime, c.author.name, c.message)
        if HWND_t != 0:
            windowborder = win32gui.GetWindowRect(HWND_t)
            cur_pos = win32api.GetCursorPos()
            state_left_new = win32api.GetKeyState(0x01)
            if state_left_new != state_left:
                if windowborder[0] < cur_pos[0] and windowborder[2] > cur_pos[0] and windowborder[1] < cur_pos[1] and windowborder[3] > cur_pos[1]:
                    drawline((cur_pos[0] - windowborder[0] - 5, cur_pos[1] - windowborder[1] - 30))
            else:
                old = ()
    except Exception as e:
        running = 0
        print("error %r" % (e))