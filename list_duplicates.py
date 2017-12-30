#!/usr/bin/env python
from storage import *

def list_duplicates(size=1024*1024):
    db = Storage(memory = False, filename = "files.db")
    db.create_indices()
    for row in db.duplicates(size):
        drow = dict(row)
        crc = drow['crc32']
        for r in db.files_by_crc32(crc):
            dr = dict(r)
            #print "%-80s (%10d)" % (dr['name'], dr['st_size'])
            print "%s" % dr['name'].encode('utf-8')
        print '-'*100

if __name__ == "__main__":
    list_duplicates(0)
