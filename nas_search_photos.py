#!/usr/bin/env python
"""
Index files in subfolder
"""

import sys
from storage import Storage
from search_storage import FindFiles

def print_duplicates(dbs):
    """
    Print duplicates with filename
    """
    for row in dbs.duplicates():
        print row

if __name__ == "__main__":

    nargs = len(sys.argv)
    if nargs < 2:
        print "I need the path to work..."
        sys.exit(1)
    
    DB2 = Storage(memory=False)
    DB2.recreate() # TODO

    __ITER__ = FindFiles(DB2)

    DB2.begin_adding_files()
    for i in range(1,nargs):
        path = sys.argv[i]
        PROBLEM_FILES = __ITER__.search(path)
        print ""
    DB2.done_adding_files()

    print "\nduplicate keys:"
    print_duplicates(DB2)

    if PROBLEM_FILES:
        print "\nproblem files:"
        print "\n".join(PROBLEM_FILES)

