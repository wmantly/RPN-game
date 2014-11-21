#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import curses
import time

screen = curses.initscr() 
curses.noecho() 
curses.curs_set(1) 
screen.keypad(1)


def welcome():
    screen.addstr("This is a Sample Curses Script\n\n")
    time.sleep(2)
    screen.addstr('''
        Press n for new user\n\n
        Press l to login
        Press Q for quit
        ''')

    while True: 
        event = screen.getch() 
        if event == ord("Q"): break
        if event == ord("n"): return False
        if event == ord("l"): return True

def login():
    screen.clear()
    screen.addstr('''Please enter your user name\n\n
        ''')
    time.sleep(5)
    return {name:'testUser',password:'testPass' }

curses.endwin()

