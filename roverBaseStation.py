# !/usr/bin/python3
import json
import socket
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("200x200")

ip = '192.168.1.175'

m0port = 50000
m1port = 50001
m2port = 50002
m3port = 50003

motorStep = 1000

def motorCommand(ip, port, isForward: bool, amount: int):
    cmd = {
        'forward': isForward,
        'amount': amount
    }

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.connect((ip, port))
    print('sending: ' + json.dumps(cmd))
    serversocket.sendall(json.dumps(cmd).encode('utf-8'))
    serversocket.close()


def forwardCallBack():
    motorCommand(ip, m0port, True, motorStep)
    motorCommand(ip, m1port, True, motorStep)
    motorCommand(ip, m2port, True, motorStep)
    motorCommand(ip, m3port, True, motorStep)


def backwardCallBack():
    motorCommand(ip, m0port, False, motorStep)
    motorCommand(ip, m1port, False, motorStep)
    motorCommand(ip, m2port, False, motorStep)
    motorCommand(ip, m3port, False, motorStep)


def turnLeftCallBack():
    # motorCommand(ip, m0port, True, motorStep)
    motorCommand(ip, m1port, True, motorStep*2)
    # motorCommand(ip, m2port, True, motorStep)
    motorCommand(ip, m3port, True, motorStep*2)


def turnRightCallBack():
    motorCommand(ip, m0port, True, motorStep*2)
    motorCommand(ip, m1port, True, motorStep)
    motorCommand(ip, m2port, True, motorStep*2)
    motorCommand(ip, m3port, True, motorStep)


# msg = messagebox.showinfo("Hello Python", "Hello World")


F = Button(top, text="Forward", command=forwardCallBack)
B = Button(top, text="Back", command=backwardCallBack)
L = Button(top, text="Left", command=turnLeftCallBack)
R = Button(top, text="Right", command=turnRightCallBack)

F.place(x=50, y=0)
B.place(x=50, y=100)
L.place(x=0, y=50)
R.place(x=75, y=50)
top.mainloop()
