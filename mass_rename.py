import glob
import os
import re

"""
Do a mass rename of files 

We find these files using a glob pattern

We rename these files using a regex. The
regex is performed on the base file name of
to extract key parts of the path. These
key parts are then used to build a new 
file name
"""

def strategy(current_name, *args):
    number = args[0]
    fullpath = os.path.realpath(current_name)
    directory = os.path.dirname(fullpath)

    filename = number + '.jpg'
    new_name = os.path.join(directory, filename)
    os.rename(current_name, new_name)

def mass_rename(regex, strategy, wildcard):
    for path in glob.glob(wildcard):

        # TODO: make this if(match := regex.match(file))
        file = os.path.basename(path)
        if(regex.match(file)):
            groups = regex.match(file).groups()
            strategy(path, *groups)

if __name__ == '__main__':
    extract_number = re.compile('frame_(\d+)_delay\-0.1s.gif')
    mass_rename(extract_number, strategy, 'C:/Users/paul_/Downloads/rocket-gif/*.gif')
