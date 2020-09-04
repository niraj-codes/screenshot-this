from tkinter import *
from tkinter import messagebox
import sqlite3


class ReturnBook:
    def return_view(self):
        self.aidd = StringVar()
        self.astudentt = StringVar()

        self.f1 = Frame(height=550, width=500, bg='black')
        self.f1.place(x=500, y=100)
        l1 = Label(self.f1, text='Book ID : ', font='papyrus 15 bold', fg='orange', bg='black').place(x=50, y=100)
        e1 = Entry(self.f1, width=25, bd=4, bg='orange', textvariable=self.aidd).place(x=180, y=100)
        l2 = Label(self.f1, text='Student Id : ', font='papyrus 15 bold', fg='orange', bg='black').place(x=50, y=150)
        e2 = Entry(self.f1, width=25, bd=4, bg='orange', textvariable=self.astudentt).place(x=180, y=150)
        b1 = Button(self.f1, text='Back', font='Papyrus 10 bold', fg='orange', bg='black', activebackground='orange',
                    activeforeground='black', width=10, bd=3, command=self.f1.destroy).place(x=50, y=250)
        b1 = Button(self.f1, text='Return', font='Papyrus 10 bold', fg='orange', bg='black', activebackground='orange',
                    activeforeground='black', width=10, bd=3, command=self.return_book).place(x=200, y=250)
        self.f1.grid_propagate(0)

    def return_book(self):
        a = self.aidd.get()
        b = self.astudentt.get()

        conn = sqlite3.connect('db/softwarica.db')

        fg = conn.execute("select ID from book_info where ID=?", (a.capitalize(),))
        fh = fg.fetchall()
        conn.commit()
        if fh != None:
            c = conn.execute("select * from book_issued where BOOK_ID=? and STUDENT_ID=?",
                             (a.capitalize(), b.capitalize(),))
            d = c.fetchall()
            conn.commit()
            if len(d) != 0:
                c.execute("DELETE FROM book_issued where BOOK_ID=? and STUDENT_ID=?",
                          (a.capitalize(), b.capitalize(),));
                conn.commit()
                conn.execute("update book_info set COPIES=COPIES+1 where ID=?", (a.capitalize(),))
                conn.commit()

                messagebox.showinfo("Success", "Book Returned sucessfully.")
            else:
                messagebox.showerror("Error", "Data not found.")
        else:
            messagebox.showerror("Error", "No such book.\nPlease add the book in database.")
        conn.commit()
        conn.close()

        
        
        
