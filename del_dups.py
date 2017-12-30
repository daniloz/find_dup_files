#!/usr/bin/env python
import os

# Generate duplicate files list with
# ./list_duplicates.py > dups.txt

filepath = 'dups.txt'  
with open(filepath) as fp:  
    line = fp.readline()
    while line:
        name = line.strip()
        if name[0] is not '-':
            print "Deleting %s -" % name,
            try:
                os.remove(name)
                print "Done"
            except OSError, e:
                print e
        line = fp.readline()
