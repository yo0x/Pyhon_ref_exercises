import sqlite3
import os

data = (("Jean-Baptise", "Human", 21),("Jean2", "sp2", 33),("Jean3", "sp3", 12))

with sqlite3.connect(':memory:') as Roster:
    c = Roster.cursor()
    c.executescript("""
        DROP TABLE IF EXISTS rroster;
        CREATE TABLE rroster(Name TEXT, Species TEXT, Iq INT);
    """)
    c.executemany("INSERT INTO rroster VALUES(?,?,?)",data)
    print ("-------------------1-----------------")
    c.execute("UPDATE rroster SET Species=? WHERE Name=? AND Iq=?", ('Human', 'Jean2', 33))
    print("-------------------2-----------------")
    c.execute("SELECT Name, Iq FROM rroster WHERE Species='Human'")
    for row in c.fetchall():
        print(row)
