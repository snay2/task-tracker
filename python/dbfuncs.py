import sqlite3
from time import time

# Dictionary factory instead of the standard row factory
def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Gets a connection to the databse
def getConnection():
    conn = sqlite3.connect('db/data.db')
    conn.row_factory = dict_factory
    return conn

# Setup the database afresh
def setup():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()
    c.execute('create table if not exists tasks (id integer primary key, name text, due text, category integer, star integer, completed integer, time integer, started integer)')
    #c.execute('insert into tasks values (NULL, "First task", "", 0, 0, 0, 0, 0)')
    #c.execute('insert into tasks values (NULL, "Second task", "", 0, 0, 0, 0, 0)')
    conn.commit()
    c.close()

######################################
# Tasks
######################################
# Get all the tasks in an array
def getAllTasks():
    conn = getConnection()
    c = conn.cursor()
    c.execute('select * from tasks where completed=0 order by due')
    list = [row for row in c]
    return list

# Add a new task to the database
def createTask(name, category, due, star):
    conn = getConnection()
    c = conn.cursor()
    star = 1 if star.lower() == 'true' else 0
    c.execute('insert into tasks values (NULL, ?, ?, ?, ?, 0, 0, 0)',\
        (name, due, category, star))
    conn.commit()
    id = c.lastrowid
    return getTask(id)

# Get a specific task from the database
def getTask(id):
    conn = getConnection()
    c = conn.cursor()
    c.execute('select * from tasks where id=?', (id,))
    list = [row for row in c]
    return list[0]

# Complete the specified task
def completeTask(id):
    conn = getConnection()
    c = conn.cursor()
    c.execute('update tasks set completed=1 where id=?', (id,))
    conn.commit()
    return getTask(id)

######################################
# Time
######################################
# Add time
def addTime(taskid, minutes):
    conn = getConnection()
    c = conn.cursor()
    task = getTask(taskid)
    newtime = int(task['time']) + minutes
    c.execute('update tasks set time=? where id=?', (newtime, taskid))
    conn.commit()
    return getTask(taskid)

# Start time
def startTime(taskid):
    conn = getConnection()
    c = conn.cursor()
    task = getTask(taskid)
    if task['started'] != 0:
        return task
    c.execute('update tasks set started=? where id=?', (int(time()), taskid))
    conn.commit()
    return getTask(taskid)

# Stop time
def stopTime(taskid):
    conn = getConnection()
    c = conn.cursor()
    task = getTask(taskid)
    if task['started'] <= 0:
        return task
    newtime = int(task['time']) + ((int(time()) - int(task['started'])) / 60)
    c.execute('update tasks set started=0, time=? where id=?', (newtime, taskid))
    conn.commit()
    return getTask(taskid)
