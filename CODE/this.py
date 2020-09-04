from tkinter import *
from tkinter import ttk
import sqlite3
from classes.createTree import CreateTree
from classes.Books.searchBooks import SearchBooks


class TestClass:

    def add_book(self, id, title, author, genre, copies, location):
        a = id
        b = title
        c = author
        d = genre
        e = copies
        f = location
        try:
            e = int(copies)
        except ValueError:
            return False
        conn = sqlite3.connect('../db/softwarica.db')
        try:
            if (a and b and c and d and f) == "":
                return False
            elif "-" in str(e):
                return False
            else:
                conn.execute("insert into book_info \
                values (?,?,?,?,?,?)",
                             (a.capitalize(), b.capitalize(), c.capitalize(), d.capitalize(), e, f.capitalize(),));
                conn.commit()
                return True

        except sqlite3.IntegrityError:
            return True

    def list_all_books(self):
        self.f1 = Frame(height=500, width=650, bg='black')
        self.f1.place(x=500, y=100)
        b1 = Button(self.f1, text='Back', fg='orange', bg='black', activebackground='orange', activeforeground='black',
                    width=10, bd=3, command=self.f1.destroy).place(x=250, y=400)
        conn = sqlite3.connect('../db/softwarica.db')
        self.list3 = ("BOOK ID", "TITLE", "AUTHOR", "GENRE", "COPIES", "LOCATION")
        self.treess = CreateTree.create_tree(self, self.f1, self.list3)
        self.treess.place(x=25, y=50)
        c = conn.execute("select * from book_info")
        g = c.fetchall()
        if len(g) != 0:
            for row in g:
                self.treess.insert('', END, values=row)
            return len(g)
        conn.commit()
        conn.close()

    def search_book(self, bookinfo):
        k = bookinfo
        if k != "":
            self.list4 = ("BOOK ID", "TITLE", "AUTHOR", "GENRE", "COPIES", "LOCATION")
            self.trees = CreateTree.create_tree(self, self.f1, self.list4)
            self.trees.place(x=25, y=150)
            conn = sqlite3.connect('../db/softwarica.db')
            c = conn.execute("select * from book_info where ID=? OR TITLE=? OR AUTHOR=? OR GENRE=?",
                             (k.capitalize(), k.capitalize(), k.capitalize(), k.capitalize(),))
            a = c.fetchall()
            if len(a) != 0:
                for row in a:
                    self.trees.insert("", END, values=row)
                conn.commit()
                conn.close()
                self.trees.bind('<<TreeviewSelect>>')
                self.variable = StringVar(self.f1)
                self.variable.set("Select Action:")

                self.cm = ttk.Combobox(self.f1, textvariable=self.variable, state='readonly', font='Papyrus 15 bold',
                                       height=50, width=15, )
                self.cm.config(values=('Add Copies', 'Delete Copies', 'Delete Book'))

                self.cm.place(x=50, y=100)
                self.cm.pack_propagate(0)

                self.combo_box = SearchBooks.combo_box
                self.cm.bind("<<ComboboxSelected>>", self.combo_box)
                self.cm.selection_clear()
                return True
            else:
                return False
        else:
            return False

    def issue_book(self, bookid, studentid):
        conn = sqlite3.connect('../db/softwarica.db')
        cursor = conn.cursor()
        cursor.execute("select ID,COPIES from book_info where ID=?", (bookid.capitalize(),))
        an = cursor.fetchall()
        if (bookid and studentid != ""):
            if an != []:
                for i in an:
                    if i[1] > 0:
                        try:
                            conn.execute("insert into book_issued \
                            values (?,?,date('now'),date('now','+7 day'))",
                                         (bookid.capitalize(), studentid.capitalize(),));
                            conn.commit()
                            conn.execute("update book_info set COPIES=COPIES-1 where ID=?", (bookid.capitalize(),))
                            conn.commit()
                            conn.close()
                            return True
                        except:
                            return False

                    else:
                        return False
            else:
                return False
        else:
            return False

    def search_all_activity(self):
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = CreateTree.create_tree(self, self.f1, self.list2)
        self.trees.place(x=50, y=150)
        conn = sqlite3.connect('../db/softwarica.db')
        try:
            c = conn.execute("select * from book_issued")
            d = c.fetchall()
            for row in d:
                self.trees.insert("", END, values=row)

            conn.commit()
            return len(d)

        except Exception as e:
            return False

    def return_book(self, bookid, studentid):
        a = bookid
        b = studentid

        conn = sqlite3.connect('../db/softwarica.db')

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

                return True
            else:
                return False
        else:
            return False

    def delete_book(self):
        conn = sqlite3.connect('../db/softwarica.db')
        cd = conn.execute("select * from book_issued where BOOK_ID=1093")
        ab = cd.fetchall()
        if ab != 0:
            conn.execute("DELETE FROM book_info where ID=1093")
            conn.commit()
            return True
        else:
            return False

        
        
