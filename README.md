# TempRepo
This used to be a temporary repo for transferring files to RPI running plan 9. I'm expanding it to include files that I want to save but don't have a good place for

# Scripts in the repo
debug:
    purpose: generate a tmux session for debugging a python script. 
             the generated session will have two windows - one in VIM
             in which the script is open, and one in PDB with the 
             script stopped and ready to be debugged
    usage: debug <script.py>
    
dedent:
    purpose: dedent (un-indent) lines in a python file. this is mostly useful
             for piping indented code into python. Input comes from stdin
    usage: cat <file.py> | dedent

pyserve: 
    purpose: start up a listening server on port 2754. the server listens for incoming
             messages (which are expected to contain python code). the server takes those
             messages, runs them through exec, and spits out their result.
             the server provides a custom global namespace in which all code is run. as a 
             result, the server maintains a history of everything defined in the global
             namespace. in other words, the server remembers the result of previous definitions.
             if you already defined a variable in a previous connection, you should be able to 
             use it in all subsequent connections (so long as it is not deleted)
    usage: pyserve
             
pyclient:
    purpose: send python messages to pyserver at port 2754. most useful as a pipe. input comes from stdin
             raises an error if nothing is listening on port 2754
    usage: cat <file.py> | pyclient
    
vimrc:
    my .vimrc. definitions in here are mostly for my own convenience. most novel commands are "r" and "p"
    in select mode (this "R"uns the selected text through the python interpreter, or "P"asses the test to
    a persisetent listening server which remembers prior definitions). the "P" command, in particular, makes
    VIM feel more like a REPL than a text editor
