# Task Tracker API
The API is RESTful and can be implemented in any language. Here are the basic
operations:

## /task/create
Creates a new task

Parameters:

* _name_ Name of the task
* _category_ (optional) Category ID
* _due_ (optional) Due date of the task
* _star_ (optional) Whether the task is starred

Returns: the task object

## /task/update
Updates data in the task (name, category, star, etc.)

Parameters:

* _id_ ID of the task to update
* _name_ (optional)
* _category_ (optional)
* _due_ (optional)
* _star_ (optional)

Returns: the updated task object

## /task/complete
Marks a task as completed. At this point it is archived but retains the same ID.

Parameters:

* _id_ ID of the task to complete

Returns: the updated task object

## /task/list
Gets a list of all the active tasks, or all the tasks in a given category

Parameters:

* _category_ (optional)

Returns: list of task objects

## /time/add
Adds time to the specified task

Parameters:

* _taskid_ ID of the task
* _minutes_ Number of minutes to add on the task

Returns: the updated task object

## /time/start
Starts the timer for a given task.

Parameters:

* _taskid_ ID of the task

Returns: the task object

## /time/stop
Stops the timer for a given task and adds the time to the task.
Using /start and /stop in conjunction has the same effect as using /add by
itself. This allows some flexibility in how the time is logged.

Parameters:

* _taskid_ ID of the task

Returns: the updated task object with elapsed time added

## /category/create
Creates a new category

Parameters:

* _name_ Name of the category

Returns: the new category object

## /category/archive
Archives a category. Operation will fail if the category has any active tasks. _Not implemented in the first version._

Parameters:

* _id_ ID of the category to archive

Returns: error object

## /category/update
Change the name of the category

Parameters:

* _id_ ID of the category to update
* _name_ (optional) New name for the category

Returns: the updated category object

## /category/list
Gets a list of all the categories

Parameters: none

Returns: a list of category objects


# JSON objects
These are the JSON objects returned by these methods

## task
    {
        "id": 000,
        "name": "string",
        "category": 000,
        "due": "string",
        "star": boolean,
        "time": 000
    }

## category
    {
        "id": 000,
        "name": "string"
    }

## error
    {
        "success": boolean,
        "message": "string"
    }
