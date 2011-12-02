import dbfuncs, json
from bottle import route, run, debug, request
from time import time

######################################
# Front end
######################################
@route('/')
def index():
    return open('front-end/index.html', 'r')

######################################
# Tasks
######################################
# List
@route('/task/list')
def taskList():
    list = dbfuncs.getAllTasks()
    return {"time": int(time()), "tasks": list}
    
# Create
@route('/task/create')
def taskCreate():
    name = request.params['name']
    category = int(request.params['category'])
    due = request.params['due']
    star = request.params['star']
    return dbfuncs.createTask(name, category, due, star)

# Complete
@route('/task/complete')
def taskComplete():
    id = int(request.params['id'])
    return dbfuncs.completeTask(id)

######################################
# Time
######################################
# Add
@route('/time/add')
def timeAdd():
    taskid = int(request.params['taskid'])
    minutes = int(request.params['minutes'])
    return dbfuncs.addTime(taskid, minutes)

# Start
@route('/time/start')
def timeStart():
    taskid = int(request.params['taskid'])
    return dbfuncs.startTime(taskid)

# Stop
@route('/time/stop')
def timeStop():
    taskid = int(request.params['taskid'])
    return dbfuncs.stopTime(taskid)

# Run the server
debug(True)
run(host='localhost', port=8080, reloader=True)
