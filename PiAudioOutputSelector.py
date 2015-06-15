#! /usr/bin/env python
# PiAudioOutputSelector.py
# Programmed by Kent Slack, copyright 2015
# Licensed under the GPL v2
#
#
# GUI module generated by PAGE version 4.5
# In conjunction with Tcl version 8.6
#    Jun 02, 2015 11:28:05 AM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import audioOutputSelect_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Audio_Output_Select')
    geom = "146x178+409+525"
    root.geometry(geom)
    w = Audio_Output_Select (root)
    audioOutputSelect_support.init(root, w)
    root.mainloop()

w = None
def create_Audio_Output_Select(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('Audio_Output_Select')
    geom = "146x178+409+525"
    w.geometry(geom)
    w_win = Audio_Output_Select (w)
    audioOutputSelect_support.init(w, w_win, param)
    return w_win

def destroy_Audio_Output_Select():
    global w
    w.destroy()
    w = None


class Audio_Output_Select:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 


        self.Frame1 = Frame(master)
        self.Frame1.place(relx=0.07, rely=0.06, relheight=0.87, relwidth=0.86)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=125)

        # Create GUI components for user interaction
        self.analogJackBtn = Radiobutton(self.Frame1)
        self.analogJackBtn.place(relx=0.08, rely=0.45, relheight=0.14
                , relwidth=0.78)
        self.analogJackBtn.configure(activebackground="#d9d9d9")
        self.analogJackBtn.configure(command=audioOutputSelect_support.analogSelected)
        self.analogJackBtn.configure(justify=LEFT)
        self.analogJackBtn.configure(text='''3.5MM Jack''')
        self.analogJackBtn.configure(value="3.5MM")
        self.analogJackBtn.deselect()

        self.hdmiBtn = Radiobutton(self.Frame1)
        self.hdmiBtn.place(relx=0.08, rely=0.58, relheight=0.14, relwidth=0.49)
        self.hdmiBtn.configure(activebackground="#d9d9d9")
        self.hdmiBtn.configure(command=audioOutputSelect_support.hdmiSelected)
        self.hdmiBtn.configure(justify=LEFT)
        self.hdmiBtn.configure(text='''HDMI''')
        self.hdmiBtn.configure(value="HDMI")
        self.hdmiBtn.deselect()

        self.autoBtn = Radiobutton(self.Frame1)
        self.autoBtn.place(relx=0.08, rely=0.32, relheight=0.14, relwidth=0.46)
        self.autoBtn.configure(activebackground="#d9d9d9")
        self.autoBtn.configure(command=audioOutputSelect_support.autoSelected)
        self.autoBtn.configure(justify=LEFT)
        self.autoBtn.configure(text='''Auto''')
        self.autoBtn.configure(value="Auto")
        self.autoBtn.deselect()

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.08, rely=0.71, height=27, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=audioOutputSelect_support.exit_function)
        self.Button1.configure(text='''Exit''')
        self.Button1.configure(width=97)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.08, rely=0.06, height=39, width=106)
        self.Label1.configure(text='''Select the Audio Source to use.''')
        self.Label1.configure(width=106)
        self.Label1.configure(wraplength="100")


if __name__ == '__main__':
    vp_start_gui()


