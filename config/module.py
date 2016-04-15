import sqlite3

# Vars
sqlite_file = 'data.db'
table_one = 'fingerprintid'
table_two = 'deviceid'
table_three = 'userid'
table_four = 'ipaddress' 
column_user = 'INTEGER'
colump_ip = 'TEXT'

# Connect
conn = sqlite3.connect(sqlite_file)
c = conn.cursor() 

#create user column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_three, nf=new_field, ft=column_user))

#create ipaddress column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_four, nf=new_field, ft=column_ip))

# Close Connection
conn.commit()
conn.close()
