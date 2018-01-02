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

    if len(sys.argv) < 2:
        print "I need the path to work..."
        sys.exit(1)
    
    path = sys.argv[1]
    print "Searching for duplicate files in %s" % path

    DB2 = Storage(memory=False)
    DB2.recreate() # TODO

    __ITER__ = FindFiles(DB2)

    DB2.begin_adding_files()
    PROBLEM_FILES = __ITER__.search(path)
    DB2.done_adding_files()

    print "\nduplicate keys:"
    print_duplicates(DB2)

    if PROBLEM_FILES:
        print "\nproblem files:"
        print "\n".join(PROBLEM_FILES)

