# !usr/bin/env python

import os,sys,tty,termios,select
msg ="""
Python keyboard monitoring!
-----------------------------
Reading from keyboard:
  W
A S D
  X
Q to exit
"""
if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    print (msg)
    while(1):
        fd = sys.stdin.fileno()
        tty.setraw(fd)
        rs, ws, es = select.select([sys.stdin], [], [], 0.1)
        if rs:
            key = sys.stdin.read(1)
        else:
            key = ' '
            # print error
        termios.tcsetattr(sys.stdin,termios.TCSADRAIN,settings)
        if key == 'w':
            print ('move forward')
        elif key == 'x':
            print ('move back')
        elif key == 'a':
            print ('move left')
        elif key == 'd':
            print ('move right')
        elif key == 's':
            print ('stop')
        elif key == 'q':
            print ('shutdown!')
            break
        elif key == '\x03':
            print ('shutdown!')
            break





