def dat_up():
    idn = first.get()
    print(idn)
    name = nme_p.get()
    des = des_p.get()
    
    table = '''CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY,name TEXT,description TEXT);'''
    cur.execute(table)
    table_data = '''INSERT INTO notes(id,name,description)
    VALUES(?,?,?)'''
    cur.execute(table_data,(idn,name,des))
    database.commit()
    cur.execute("SELECT * from notes;")
    res = cur.fetchall()
    print(res)
    return database
    
    cur.close()
    database.close()
