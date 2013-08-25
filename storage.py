#!/usr/bin/env python
import sqlite3 as lite
import sys, os
import subprocess
import string

class Storage:
    def __init__(self):
        #self.con = lite.connect('files.db')
    def __init__(self, memory):
        if memory:
            self.con = lite.connect(':memory:')
            create_db()
        else:
            self.con = lite.connect('files.db')
        self.con.row_factory = lite.Row
        #self.con.text_factory = str

    def recreate(self):
        self.create_db()

    def create_db(self):
        cur = self.con.cursor()
        cur.execute("DROP TABLE IF EXISTS Files")
        cur.execute("CREATE TABLE Files(SHA1 TEXT, Name TEXT)")
        self.con.commit();


    def add_file(self, sha1, name):
        try:
            cur = self.con.cursor()
            cur.execute("INSERT INTO Files VALUES(?, ?)", (sha1, name))
            self.con.commit();
        except lite.Error, e:
            print "Error %s: name: %s" % (e.args[0], name)
            self.con.rollback()

    def dump(self):
        for line in self.con.iterdump():
            print line

    def duplicates(self):
        cur = self.con.cursor()
        return cur.execute("SELECT COUNT(*) Count, sha1, Name FROM Files GROUP BY \
                           sha1 HAVING COUNT(*) > 1 ORDER BY COUNT(*) DESC")

    def filenames(self, sha1):
        cur = self.con.cursor()
        return cur.execute("SELECT sha1, Name FROM Files WHERE sha1 = ?", (sha1,))


def build_test_corpus(db):
    print "test_corpus"
    db.add_file('9db39b5c8b9eb70149801f8c9112c3ef50dcd562', 'ida_-_Vylet_na_prehradu/IMAG0167.jpg')
    db.add_file('9db39b5c8b9eb70149801f8c9112c3ef50dcd562', 'et_na_prehradu/IM.jpg')
    db.add_file('9db39b5c8b9eb70149801f8c9112c3ef50dcd562', '_na_prehradu/IM.jpg')
    db.add_file('9db39b5c8b9eb70149801f8c9112c3ef50dcd565', 'erehradu/IM.jpg')
    db.add_file('881d34fd4fc2d55af571e9f8c587108bf4d45ea2','cii_Empik_hleda_Foxika/P1080538.jpg')
    db.add_file('881d34fd4fc2d55af571e9f8c587108bf4d45ea2','i_Empik_hleda_Foxika/P1080538.jpg')
    db.add_file('881d34fd4fc2d55af571e9f8c587108bf4d45ea5','i_E_Foxika/P1080538.jpg')


if __name__ == "__main__":
    db = Storage(memory=True)
    build_test_corpus(db)
    #print db
    #print len(db.all_rows())

    print "\ncollisions"
    for row in db.duplicates():
        print row

    print "\nfiles for one sha1"
    for row in db.filenames('9db39b5c8b9eb70149801f8c9112c3ef50dcd562'):
        print row
