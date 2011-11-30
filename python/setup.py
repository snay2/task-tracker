import dbfuncs
# Setup the database
dbfuncs.setup()
conn = dbfuncs.getConnection()
c = conn.cursor()
c.execute('select * from tasks')
for row in c:
    print row
c.close()

