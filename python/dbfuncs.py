import sqlite3

# Gets a connection to the databse
def getConnection():
    return sqlite3.connect('db/data.db')

# Setup the database afresh
def setup():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()
    c.execute('create table if not exists tasks (id integer primary key, name text, due text, category integer, star integer, completed integer)')
    c.execute('insert into tasks values (NULL, "First task", "", 0, 0, 0)')
    c.execute('insert into tasks values (NULL, "Second task", "", 0, 0, 0)')
    conn.commit()
    c.close()

# Get all the tasks in an array
def getAllTasks():
    conn = getConnection()
    c = conn.cursor()
    c.execute('select * from tasks where completed=0')
    list = []
    for row in c:
        (id, name, due, category, star, completed) = row
        obj = {"id": id, \
            "name": name, \
            "due": due, \
            "category": category, \
            "star": star \
        }
        list.append(obj)
    return list


