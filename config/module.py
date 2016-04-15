import sqlite3

class Module:

    def save(userid, deviceid, ipaddress):
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE fingerprintid
             (userid text, deviceid text, ipaddress text)''')
        c.execute("INSERT INTO fingerprintid VALUES (?,?,?)", userid, deviceid, ipaddress)
        conn.commit()
        conn.close()
        return
