#!/usr/bin/python

import os
import pathlib

def get_filename_index(filename):
    dot_index = filename.find('.') # the numbers before the file extension is the index of the recording
    
    if dot_index < 2 or dot_index == -1:
        return 0 # won't change anything
    
    # get 2 characters before the dot
    char1 = filename[dot_index - 2]
    char2 = filename[dot_index - 1]
        
    # return a number
    try:
        return int(char1 + char2)
    except ValueError:
        return 0

dirname = os.getcwd()

# get the highest file number
highest = 0;
for filename in os.listdir(dirname):
    filename_index = get_filename_index(filename)
        
    if filename_index > highest:
        highest = filename_index
        
new_index = f'{highest + 1}'.zfill(2)
new_filename = f'{os.path.basename(dirname)}-{new_index}.mp3'

# record and compress
print('Press Ctrl + C to stop recording.')
os.system(f'arecord -v -f cd -t raw | lame -r -b 64 - {new_filename}')

# play back
os.system(f'mpv {new_filename}')
