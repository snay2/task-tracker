# Task Tracker API
The API is RESTful and can be implemented in any language. Here are the basic
operations:

## /task/new
Creates a new task

## /task/update
Updates data in the task (title, category, priority, etc.)

## /task/complete
Marks a task as completed. At this point it is archived but retains the same ID.

## /time/add
Adds time to the specified task

## /time/start
Starts the timer for a given task.

## /time/stop
Stops the timer for a given task and adds the time to the task.
Using /start and /stop in conjunction has the same effect as using /add by
itself. This allows some flexibility in how the time is logged.

## /time/total
Gets the total expended time on a given task or category

## /category/create
Creates a new category

## /category/archive
Archives a category. Operation will fail if the category has any active tasks.

## /category/update
Change the name of the category

## /category/list
Gets a list of all the categories

## /task/list
Gets a list of all the active tasks, or all the tasks in a given category

