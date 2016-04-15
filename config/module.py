import sqlite3

# Vars
sqlite_file = 'data.db'
table_one = 'fingerprintid'
table_two = 'deviceid'
table_three = 'userid'
table_four = 'ipaddress' 

# Connect
conn = sqlite3.connect(sqlite_file)
c = conn.cursor() 

# Close Connection
conn.commit()
conn.close()
