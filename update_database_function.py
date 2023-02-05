def dat_up():
    #getting user input from GUI
    idn = first.get()
    name = nme_p.get()
    des = des_p.get()
    
    
    table = '''CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY,name TEXT,description TEXT);'''### creating the table
    cur.execute(table)
    table_data = '''INSERT INTO notes(id,name,description)
    VALUES(?,?,?)'''# adding or updating table values
    cur.execute(table_data,(idn,name,des))
    database.commit()
    cur.execute("SELECT * from notes;")
    res = cur.fetchall()# printing database in console if required
    print(res)
    return database
    
    cur.close()
    database.close()
