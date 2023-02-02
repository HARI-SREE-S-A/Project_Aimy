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
