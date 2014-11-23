#!/usr/bin/env python3



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

    

def login():
    screen.clear()
    screen.addstr('''Please enter your user name\n\n
        ''')
    time.sleep(5)
    return {name:'testUser',password:'testPass' }

curses.endwin()






import curses

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print( " ")
     if a == 0:
          print( "Command executed correctly" )
     else:
          print( "Command terminated with error")
     raw_input("Press enter")
     print( "" )

x = 0

while x != ord('4'):
     screen = curses.initscr()

     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, "Please enter a number...")
     screen.addstr(4, 4, "1 - Add a user")
     screen.addstr(5, 4, "2 - Restart Apache")
     screen.addstr(6, 4, "3 - Show disk space")
     screen.addstr(7, 4, "4 - Exit")
     screen.refresh()

     x = screen.getch()

     if x == ord('1'):
          username = get_param("Enter the username")
          homedir = get_param("Enter the home directory, eg /home/nate")
          groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
          shell = get_param("Enter the shell, eg /bin/bash:")
          curses.endwin()
          execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
     if x == ord('2'):
          curses.endwin()
          execute_cmd("apachectl restart")
     if x == ord('3'):
          curses.endwin()
          execute_cmd("df -h")

curses.endwin()