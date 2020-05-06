#!/usr/bin/python3

from time import sleep


import pty
import os
import time
import sys
import select
import fcntl

(pty_master, pty_slave) = pty.openpty()
tty = os.ttyname(pty_slave)

if os.path.islink('/tmp/kiss_pty'):
        os.unlink('/tmp/kiss_pty')
os.symlink(tty, '/tmp/kiss_pty')


print ('KISS PTY is: /tmp/kiss_pty (%s)' % os.ttyname(pty_slave))

#os.dup2(pty_master, 0)
#os.dup2(pty_master, 1)
#os.dup2(pty_slave, 2)



# To shell
term_w = os.fdopen(pty_master, 'w')
term_r = os.fdopen(pty_master, 'r')


# To ehm, other shell
STDIN_FD = sys.stdin.fileno()


fcntl.fcntl(pty_master, fcntl.F_SETFL, os.O_NONBLOCK)
last_output = ["undef"]
while True:
	rfds, wfds, xfds = select.select([pty_master, STDIN_FD], [], [])

	# Incomming from shell
	if pty_master in rfds:
		line = term_r.readline().strip()
		print("Recv line from shell: {}".format(line))
		last_output.append(line)
	
	# Incomming from stdin to this script
	if STDIN_FD in rfds:
		line = sys.stdin.readline().strip()
		if line == "#1":
			print(" - LOCAL CM - getting last output")
			print(last_output)
		else:
			print("Recv line stdin: '{}'".format(line))
			term_w.write(line + "\n")
			last_output = []




#while True:
#	line = sys.stdin.readline().strip()
#	if line == "TEST":
#		print("this never reached the SHELL, just relay-shell")
#	else:
#		term_w.write(line + "\n")
#
#	line = term_r.readline()
#	print("OUTPUT: {}".format(line))

