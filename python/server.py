import dbfuncs, json
from bottle import route, run, debug, request

# Test page
@route('/')
def index():
    return "All systems nominal."

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
