# task-tracker: Python
This is a Python implementation of the API.

It runs on Bottle and uses a SQLite database as the back-end.

## Setup
Run `python setup.py` to create and set up the database. That creates
a `data.db` file in the `db/` subdirectory.

## Running the server
There are two steps to run the server. The first is `python server.py`. This starts
the Bottle server on its default port.

The second step is optional. It involves my fork of
[localtunnel](https://github.com/snay2/localtunnel), which allows you to expose the
locally-running server outside your network.
Run `./tunnel.rb` from the command line. The script takes two arguments: the port 
and (optionally) the URL that should be pinged to notified when the tunnel is created.
I use this to notify a Kynetx app that the server is running and where to find it.

You can change the port the Bottle server runs on by editing the configuration
at the bottom of the `server.py` source.

