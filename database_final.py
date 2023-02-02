from tkinter import *
from tkinter import messagebox
import sqlite3
database = sqlite3.connect("demo_data.db")
cur = database.cursor()



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

root = Tk()
root.title("Welcome")
root.geometry("600x600")
root.resizable(True,True)

def view():
    frame = Tk()
    frame.geometry("700x700")
    frame.title("data")
    r_set  = database.execute("SELECT * from notes;")
    i = 0
    for notes in r_set:
        for j in range(len(notes)):
            e = Entry(frame, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, notes[j])
           
        i=i+1
###########################################################################################
id_ = Label(root,text = 'enter your id',fg = 'blue',font = ('Calibri(body)',12,'bold'))
id_.place(x = 50,y = 150)
first = Entry(root,width = 25,bg = 'white',border = 5,fg ='black',font=('Calibri(body)',12))
first.place(x = 200,y = 150)
##########################################################################################
nme = Label(root,text = 'enter your name',fg = 'blue',font = ('Calibri(body)',12,'bold'))
nme.place(x = 50,y = 250)
nme_p =  Entry(root,width = 25,bg = 'white',border = 5,fg ='black',font=('Calibri(body)',12))
nme_p.place(x = 200,y = 250)
##########################################################################################
des = Label(root,text = 'enter description',fg = 'blue',font = ('Calibri(body)',12,'bold'))
des.place(x = 50,y = 350)
des_p = Entry(root,width = 25,bg = 'white',border = 5,fg ='black',font=('Calibri(body)',12))
des_p.place(x = 200,y = 350)
#########################################################################################
updt = Button(root,text = "update database",width = 20,fg = 'white',bg = 'blue',command = dat_up)
updt.place(x = 100,y = 500)
###########################################################################################
viewb = Button(root,text = "View",width = 15,fg = 'white',bg = 'blue',command = view)
viewb.place(x = 300,y = 500)


root.mainloop()

