from tkinter import *
import sqlite3
from classes.createTree import CreateTree


class AllBooks:
    def list_all_books(self):
        self.f1 = Frame(height=500, width=650, bg='black')
        self.f1.place(x=500, y=100)
        b1 = Button(self.f1, text='Back', fg='orange', bg='black', activebackground='orange', activeforeground='black',
                    width=10, bd=3, command=self.f1.destroy).place(x=250, y=400)
        conn = sqlite3.connect('db/softwarica.db')
        self.list3 = ("BOOK ID", "TITLE", "AUTHOR", "GENRE", "COPIES", "LOCATION")
        self.treess = CreateTree.create_tree(self, self.f1, self.list3)
        self.treess.place(x=25, y=50)
        c = conn.execute("select * from book_info")
        g = c.fetchall()
        if len(g) != 0:
            for row in g:
                self.treess.insert('', END, values=row)
        conn.commit()
        conn.close()

        
        
        
