# task-tracker: Python
This is a Python implementation of the API.

It runs on Bottle and uses a SQLite database as the back-end.

## Setup
Run `python setup.py` to create and set up the database. That creates
a `data.db` file in the `db/` subdirectory.

## Running Bottle
Run `python server.py` from the command line. This will start a Bottle server
on port 8080. You can modify the port by editing the Bottle configuration
at the bottom of the `server.py` source.

