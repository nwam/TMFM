import sys
import os

def loop_files(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for filename in files:
            yield subdir + os.sep + filename
