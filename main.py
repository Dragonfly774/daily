# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('project_db.db')

cur = con.cursor()
name = [2, 'popa', 4, 4, 4]

print(cur.execute('SELECT * FROM Data').fetchall())

# for i in result:
#     print(i[0])
