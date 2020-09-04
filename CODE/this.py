from tkinter import *
from tkinter import messagebox
import sqlite3
from classes.searchingSortingAlgorithm import SearchingSorting


class IssueBook:
    def issue_view(self):
        self.aidd = StringVar()
        self.astudentt = StringVar()
        self.f1 = Frame(height=550, width=500, bg='black')
        self.f1.place(x=500, y=100)
        l1 = Label(self.f1, text='Book ID : ', font='papyrus 15 bold', bg='black', fg='orange').place(x=50, y=100)
        e1 = Entry(self.f1, width=25, bd=4, bg='orange', textvariable=self.aidd).place(x=180, y=100)
        l2 = Label(self.f1, text='Student Id : ', font='papyrus 15 bold', bg='black', fg='orange').place(x=50, y=150)
        e2 = Entry(self.f1, width=25, bd=4, bg='orange', textvariable=self.astudentt).place(x=180, y=150)
        b1 = Button(self.f1, text='Back', font='Papyrus 10 bold', fg='orange', bg='black', activebackground='orange',
                    activeforeground='black', width=10, bd=3, command=self.f1.destroy).place(x=50, y=250)
        b1 = Button(self.f1, text='Issue', font='Papyrus 10 bold', fg='orange', bg='black', activebackground='orange',
                    activeforeground='black', width=10, bd=3, command=self.issue_book).place(x=200, y=250)

    def issue_book(self):
        bookid = self.aidd.get()
        studentid = self.astudentt.get()
        conn = sqlite3.connect('db/softwarica.db')
        cursor = conn.cursor()

        #######manual
        cursor.execute("select ID from book_info")
        id_db_list = cursor.fetchall()
        id_list = []

        position = 0
        while position < len(id_db_list):
            id_list.append(id_db_list[position][0])
            position = position + 1
        SearchingSorting.selection_sort(self, id_list)
        if SearchingSorting.linear_search(self, bookid, id_list):
            ##########################
            cursor.execute("select ID,COPIES from book_info where ID=?", (bookid.capitalize(),))
            an = cursor.fetchall()
            if bookid and studentid != "":
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
                                messagebox.showinfo("Updated", "Book Issued sucessfully.")
                            except:
                                messagebox.showerror("Error", "Book is already issued by student.")

                        else:
                            messagebox.showerror("Unavailable", "Book unavailable.\nThere are 0 copies of the book.")
                else:
                    messagebox.showerror("Error", "No such Book in Database.")
            else:
                messagebox.showerror("Error", "Fields cannot be blank.")
        else:
            messagebox.showerror("Unavailable", "Book unavailable.")
