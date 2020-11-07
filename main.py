# -*- coding: utf-8 -*-
import sqlite3


def save_notes_data(pop):
    con = sqlite3.connect('project_db.db')
    cur = con.cursor()
    pop = pop.split()
    pole = ['id', 'section', 'data', 'datetime', 'category']
    pv = ['?', '?', '?', '?', '?']
    v = '?'
    pvv = []
    # INSERT INTO имя_таблицы(названия_полей*) VALUES(значения)
    for i in range(len(pop)):
        pvv.append(v)
    a, b = ', '.join(pole), ', '.join(pvv)
    r = cur.execute(f"INSERT OR IGNORE INTO Data({a}) VALUES({b})",
                    (pop[0], pop[1], pop[2], pop[3], pop[4])).fetchall()
    con.commit()
    con.close()
# 5 2 popapi 4.1 4
