



from tkinter import *
from tkinter import messagebox
import sqlite3


class AddBooks:
    def add_book_view(self):
        self.aid = StringVar()
        self.aauthor = StringVar()
        self.aname = StringVar()
        self.acopies = StringVar()
        self.agenre = StringVar()
        self.aloc = StringVar()
        self.f1 = Frame(height=500, width=650, bg='black')
        self.f1.place(x=500, y=100)
        l1 = Label(self.f1, text='Book ID : ', font='Papyrus 12 bold', fg='Orange', bg='Black', pady=1).place(x=50,
                                                                                                              y=50)
        e1 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aid).place(x=150, y=50)
        l2 = Label(self.f1, text='Title : ', font='Papyrus 12 bold', fg='Orange', bg='Black', pady=1).place(x=50, y=100)
        e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aname).place(x=150, y=100)
        l3 = Label(self.f1, text='Author : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                             y=150)
        e3 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aauthor).place(x=150, y=150)
        l4 = Label(self.f1, text='Genre : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50, y=200)
        e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.agenre).place(x=150, y=200)
        l4 = Label(self.f1, text='Copies : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                             y=250)
        e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.acopies).place(x=150, y=250)
        l5 = Label(self.f1, text='Location : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                               y=300)
        e3 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aloc).place(x=150, y=300)
        self.f1.grid_propagate(0)
        b1 = Button(self.f1, text='Add', font='Papyrus 10 bold', fg='orange', bg='black', activebackground='orange',
                    activeforeground='black', width=15, bd=3, command=self.add_book).place(x=150, y=400)
        b2 = Button(self.f1, text='Back', font='Papyrus 10 bold', fg='orange', bg='black', activebackground='orange',
                    activeforeground='black', width=15, bd=3, command=self.f1.destroy).place(x=350, y=400)

    ################

    def add_book(self):
        a = self.aid.get()
        b = self.aname.get()
        c = self.aauthor.get()
        d = self.agenre.get()
        e = self.acopies.get()
        try:
            e = int(e)
        except ValueError:
            messagebox.showerror("Error", "No. of copies expects integer value")
            return
        f = self.aloc.get()
        conn = sqlite3.connect('db/softwarica.db')
        try:
            if (a and b and c and d and f) == "":
                messagebox.showerror("Error", "Fields cannot be empty")
            elif "-" in str(e):
                messagebox.showerror("Error", "No. of copies cannot be negative")
            else:
                conn.execute("insert into book_info \
                values (?,?,?,?,?,?)",
                             (a.capitalize(), b.capitalize(), c.capitalize(), d.capitalize(), e, f.capitalize(),))
                conn.commit()
                messagebox.showinfo("Success", "Book added successfully")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Book is already present.")

        conn.close()

        
        
