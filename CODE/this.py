from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from classes.createTree import CreateTree


class SearchBooks:
    def search_view(self):
        self.sid = StringVar()
        self.f1 = Frame(height=500, width=650, bg='black')
        self.f1.place(x=500, y=100)
        l1 = Label(self.f1, text='Book ID/Title/Author/Genre: ', font=('Papyrus 10 bold'), bd=2, fg='orange',
                   bg='black').place(x=20, y=40)
        e1 = Entry(self.f1, width=25, bd=5, bg='orange', fg='black', textvariable=self.sid).place(x=260, y=40)
        b1 = Button(self.f1, text='Search', fg='#FFA500', bg='black', activebackground='orange',
                    activeforeground='black', font='Papyrus 10 bold', width=9, bd=2, command=self.search_book).place(
            x=500, y=37)
        b1 = Button(self.f1, text='Back', fg='#FFA500', bg='black', activebackground='orange', activeforeground='black',
                    font='Papyrus 10 bold', width=10, bd=2, command=self.f1.destroy).place(x=250, y=450)

    def search_book(self):
        k = self.sid.get()
        if k != "":
            self.list4 = ("BOOK ID", "TITLE", "AUTHOR", "GENRE", "COPIES", "LOCATION")
            self.trees = CreateTree.create_tree(self, self.f1, self.list4)
            self.trees.place(x=25, y=150)
            conn = sqlite3.connect('db/softwarica.db')

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

                self.cm.bind("<<ComboboxSelected>>", self.combo_box)
                self.cm.selection_clear()
            else:
                messagebox.showerror("Error", "Data not found")



        else:
            messagebox.showerror("Error", "Search field cannot be empty.")

    def combo_box(self, event):
        self.var_Selected = self.cm.current()
        if self.var_Selected == 0:
            self.copies_view(self.var_Selected)
        elif self.var_Selected == 1:
            self.copies_view(self.var_Selected)
        elif self.var_Selected == 2:
            self.delete_book_view()

    def delete_book_view(self):
        try:
            self.curItem = self.trees.focus()
            self.c1 = self.trees.item(self.curItem, "values")[0]
            b1 = Button(self.f1, text='Update', font='Papyrus 10 bold', width=9, bd=3, command=self.delete_book).place(
                x=500, y=97)

        except:
            messagebox.showinfo("Empty", "Please select something.")

    def delete_book(self):
        conn = sqlite3.connect('db/softwarica.db')
        cd = conn.execute("select * from book_issued where BOOK_ID=?", (self.c1,))
        ab = cd.fetchall()
        if ab != 0:
            conn.execute("DELETE FROM book_info where ID=?", (self.c1,));
            conn.commit()
            messagebox.showinfo("Successful", "Book Deleted sucessfully.")
            self.trees.delete(self.curItem)
        else:
            messagebox.showwarning("Error", "Book is Issued.\nBook cannot be deleted.")
        conn.commit()
        conn.close()

    def copies_view(self, varr):
        try:
            curItem = self.trees.focus()
            self.c1 = self.trees.item(curItem, "values")[0]
            self.c2 = self.trees.item(curItem, "values")[4]
            self.scop = IntVar()
            self.e5 = Entry(self.f1, width=20, textvariable=self.scop)
            self.e5.place(x=310, y=100)
            if varr == 0:
                b5 = Button(self.f1, text='Update', font='Papyrus 10 bold', bg='orange', fg='black', width=9, bd=3,
                            command=self.add_copies).place(x=500, y=97)
            if varr == 1:
                b6 = Button(self.f1, text='Update', font='Papyrus 10 bold', bg='orange', fg='black', width=9, bd=3,
                            command=self.delete_copies).place(x=500, y=97)
        except:
            messagebox.showinfo("Empty", "Please select something.")

    def add_copies(self):
        no = self.e5.get()
        if int(no) >= 0:

            conn = sqlite3.connect('db/softwarica.db')

            conn.execute("update book_info set COPIES=COPIES+? where ID=?", (no, self.c1,))
            conn.commit()

            messagebox.showinfo("Updated", "Copies added sucessfully.")
            self.search_book()
            conn.close()

        else:
            messagebox.showerror("Error", "No. of copies cannot be negative.")

    def delete_copies(self):
        no1 = self.e5.get()
        if int(no1) >= 0:
            if int(no1) <= int(self.c2):
                conn = sqlite3.connect('db/softwarica.db')

                conn.execute("update book_info set COPIES=COPIES-? where ID=?", (no1, self.c1,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Updated", "Deleted sucessfully")
                self.search_book()

            else:
                messagebox.showerror("Maximum", "No. of copies to delete exceed available copies.")
        else:
            messagebox.showerror("Error", "No. of copies cannot be negative.")

            
            
            
