#!/usr/bin/python3
import pty
import os
import time

(pty_master, pty_slave) = pty.openpty()
tty = os.ttyname(pty_slave)

if os.path.islink('/tmp/kiss_pty'):
	os.unlink('/tmp/kiss_pty')
os.symlink(tty, '/tmp/kiss_pty')


print ('KISS PTY is: /tmp/kiss_pty (%s)' % os.ttyname(pty_slave))

os.dup2(pty_master, 0)
os.dup2(pty_master, 1)
#os.dup2(pty_slave, 2)


while True:
	print("Print dimz")
	time.sleep(1)

