# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('project_db.db')
cur = con.cursor()

name = input().split()

pole = ['id', 'section', 'data', 'datetime', 'category']
pv = ['?', '?', '?', '?', '?']
v = '?'
pvv =[]
# INSERT INTO имя_таблицы(названия_полей*) VALUES(значения)

for i in range(len(name)):
    pvv.append(v)
a, b = ', '.join(pole), ', '.join(pvv)

r = cur.execute(f"INSERT OR IGNORE INTO Data({a}) VALUES({b})", (name[0], name[1], name[2], name[3], name[4])).fetchall()



con.commit()
con.close()

# 5 2 popapi 4.1 4
