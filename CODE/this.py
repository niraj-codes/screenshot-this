from tkinter import *
from tkinter import messagebox
import sqlite3
from classes.createTree import CreateTree


class AllActivity:
    def activity_view(self):
        self.aidd = StringVar()
        self.astudentt = StringVar()
        self.f1 = Frame(height=550, width=500, bg='black')
        self.f1.place(x=500, y=80)
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = CreateTree.create_tree(self, self.f1, self.list2)
        self.trees.place(x=50, y=150)

        l1 = Label(self.f1, text='Book/Student ID : ', font='Papyrus 15 bold', fg='Orange', bg='black').place(x=50,
                                                                                                              y=30)
        e1 = Entry(self.f1, width=20, bd=4, bg='orange', textvariable=self.aidd).place(x=280, y=35)
        b1 = Button(self.f1, text='Back', bg='orange', font='Papyrus 10 bold', width=10, bd=3,
                    command=self.f1.destroy).place(x=340, y=450)
        b1 = Button(self.f1, text='Search', bg='orange', font='Papyrus 10 bold', width=10, bd=3,
                    command=self.search_activity).place(x=40, y=450)
        b1 = Button(self.f1, text='All', bg='orange', font='Papyrus 10 bold', width=10, bd=3,
                    command=self.search_all_activity).place(x=190, y=450)
        self.f1.grid_propagate(0)

    def search_activity(self):
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = CreateTree.create_tree(self, self.f1, self.list2)
        self.trees.place(x=50, y=150)
        conn = sqlite3.connect('db/softwarica.db')
        bid = self.aidd.get()
        try:
            c = conn.execute("select * from book_issued where BOOK_ID=? or STUDENT_ID=?",
                             (bid.capitalize(), bid.capitalize(),))
            d = c.fetchall()
            if len(d) != 0:
                for row in d:
                    self.trees.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "Data not found.")
            conn.commit()

        except Exception as e:
            messagebox.showwarning(e)
        conn.close()

    def search_all_activity(self):
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = CreateTree.create_tree(self, self.f1, self.list2)
        self.trees.place(x=50, y=150)
        conn = sqlite3.connect('db/softwarica.db')
        try:
            c = conn.execute("select * from book_issued")
            d = c.fetchall()
            for row in d:
                self.trees.insert("", END, values=row)

            conn.commit()

        except Exception as e:
            messagebox.showwarning(e)
        conn.close()

        
        
