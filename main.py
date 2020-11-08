# -*- coding: utf-8 -*-
import sqlite3
import datetime as dt

print(dt.datetime.now())


def save_notes_data(info):
    con = sqlite3.connect('project_db.db')
    cur = con.cursor()
    pole = ['id', 'section', 'data', 'datetime', 'category']
    # pv = ['?', '?', '?', '?', '?']
    # v = '?'
    # pvv = []
    # # INSERT INTO имя_таблицы(названия_полей*) VALUES(значения)
    # for i in range(len(pop)):
    #     pvv.append(v)
    # a, b = ', '.join(pole), ', '.join(pvv)
    datetime = dt.datetime.now()
    cur.execute(f"INSERT INTO Data(section, data, datetime, category) VALUES(1, ?, ?, 5)", (info, datetime)).fetchall()
    con.commit()
    con.close()
    # 5 2 popapi 4.1 4
