import dbfuncs, json
from bottle import route, run, debug, request

######################################
# Front end
######################################
@route('/')
def index():
    return open('front-end.html', 'r')

######################################
# Tasks
######################################
# List
@route('/task/list')
def taskList():
    list = dbfuncs.getAllTasks()
    return {"tasks": list}
    
# Create
@route('/task/create')
def taskCreate():
    name = request.params['name']
    category = request.params['category']
    due = request.params['due']
    star = request.params['star']
    return dbfuncs.createTask(name, category, due, star)

# Complete
@route('/task/complete')
def taskComplete():
    id = request.params['id']
    return dbfuncs.completeTask(id)

# Run the server
debug(True)
run(host='localhost', port=8080, reloader=True)
