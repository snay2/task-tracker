# task-tracker: Python
This is a Python implementation of the API.

It runs on Bottle and uses a SQLite database as the back-end.

## Setup
Run `python setup.py` to create and set up the database. That creates
a `data.db` file in the `db/` subdirectory.

## Running the server
To start the server, run `python server.py`. This starts the Bottle server on its
default port.

You can change the port the Bottle server runs on by editing the configuration
at the bottom of the `server.py` source.

