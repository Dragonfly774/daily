import sqlite3


def deleting_identical_notes():
    """удаление повторых сохранненых заметок для заметок"""
    con = sqlite3.connect('project_db.db')
    cur = con.cursor()
    r = cur.execute("SELECT section, data, category FROM Data")
    db = []
    for i in r:
        db.append(i)
    del_count = []
    for i in range(len(db) - 1):
        if db[i] == db[i + 1]:
            del_count.append(1)
        else:
            del_count.append(0)
    con_2 = sqlite3.connect('project_db.db')
    cur_2 = con.cursor()
    r_2 = cur.execute("SELECT id, datetime FROM Data")
    del_data_count = []
    for i in r_2:
        del_data_count.append(i)
    del_data = []
    for i in range(len(del_count)):
        if del_count[i] == 1:
            if del_data_count[i][0] < del_data_count[i + 1][0]:
                del_data.append(del_data_count[i][0])
    for i in range(len(del_data)):
        cur_2.execute("DELETE FROM Data WHERE id = ?", (del_data[i],))
    con.commit()
    con.close()


def deleting_identical_calendar():
    """удаление повторых сохранненых заметок для календаря"""
    con = sqlite3.connect('project_db.db')
    cur = con.cursor()
    r = cur.execute("SELECT id, data, datetime FROM calendar")
    db = []
    for i in r:
        db.append(i)
    db_id = []
    db_data = []
    db_datetime = []
    for i in range(len(db)):
        db_id.append(db[i][0])
        db_data.append(db[i][1])
        db_datetime.append(db[i][2])
    for i in range(len(db) - 1):
        if db_data[i + 1] == db[i][1]:
            cur.execute("DELETE FROM calendar WHERE id = ?", (db_id[i],))
    con.commit()
    con.close()


def main():
    deleting_identical_notes()


def main_calendar():
    deleting_identical_calendar()
