import dbfuncs, json
from bottle import route, run, debug

# Test page
@route('/')
def index():
    return "All systems nominal."

# List page
@route('/task/list')
def taskList():
    list = dbfuncs.getAllTasks()
    return json.JSONEncoder().encode(list)
    

# Run the server
debug(True)
run(host='localhost', port=8080, reloader=True)
