## Howto

1. Either put path to relay_shell.py in /etc/password OR if using simpleterminal, run 
```
./st -e /path/to/relay-shell.py
```
Or just run ./relay-shell.py from an existing shell...

2. It creates a pty with a symlink (/tmp/kiss_pty). Open a new shell, and connect the newly created pty to stdin and stdout of the new shell
```
exec > /tmp/kiss_pty && exec < /tmp/kiss_pty 
```
(You can add stderr if you’d like)

3. When entering commands at the relay-shell.py you will see debugging output and the reply from the shell created from step 2.
The output is very messy.


### TODO:

1. Relay-shell.py should fork the shell 
2. Better enterpretation of command output (from shell) and command inut(from terminal emulator)
3. Impl. way to access previous commands output, fx. #1v - get output from last command and open in vim
4. Open VIM to edit output from command

