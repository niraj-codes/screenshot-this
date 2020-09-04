class Menu:

    def __init__(self):
        self.root = Tk()
        self.root.title('DASHBOARD')
        self.root.state('normal')
        conn = sqlite3.connect('db/softwarica.db')
        conn.execute('''create table if not exists book_info
        (ID VARCHAR PRIMARY KEY NOT NULL,
        TITLE VARTEXT NOT NULL,
        AUTHOR VARTEXT NOT NULL,
        GENRE VARTEXT NOT NULL,
        COPIES VARINT NOT NULL,
        LOCATION VARCHAR NOT NULL);''')
        conn.commit()
        conn.execute('''create table if not exists book_issued
        (BOOK_ID VARCHAR NOT NULL,
        STUDENT_ID VARCHAR NOT NULL,
        ISSUE_DATE DATE NOT NULL,
        RETURN_DATE DATE NOT NULL,
        PRIMARY KEY (BOOK_ID,STUDENT_ID));''')
        conn.commit()
        conn.close()
        self.a = self.canvases(image1)
        l1 = Button(self.a, text='BOOK DATA', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=19, padx=10, borderwidth=0,
                    command=self.books_menu).place(x=100, y=500)
        l2 = Button(self.a, text='STUDENT DATA', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=19, padx=10, borderwidth=0,
                    command=self.students_menu).place(x=800, y=500)

        exit = Button(self.a, text='Exit', font='Papyrus 16 bold', bg='black', fg='red', activebackground='red',
                      activeforeground='black', width=3, padx=5, borderwidth=0, command=self.root.destroy).place(x=610,
                                                                                                                 y=670)

        self.root.mainloop()

    def canvases(self, images):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        photo = Image.open(images)
        photo1 = photo.resize((w, h), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(photo1)

        # ====================================================================================
        self.canvas = Canvas(self.root, width='%d' % w, height='%d' % h)
        self.canvas.grid(row=0, column=0)
        self.canvas.grid_propagate(0)
        self.canvas.create_image(0, 0, anchor=NW, image=photo2)
        self.canvas.image = photo2
        return self.canvas

    def main_menu(self):
        self.root.destroy()
        a = Menu()

    def books_menu(self):
        self.a.destroy()
        self.a = self.canvases(image2)
        l1 = Button(self.a, text='Add Books', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=15, padx=10,
                    command=self.add_book_view).place(x=12, y=100)
        l2 = Button(self.a, text='Search Books', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=15, padx=10,
                    command=self.search_view).place(x=12, y=200)

        l4 = Button(self.a, text='All Books', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=15, padx=10,
                    command=self.list_all_books).place(x=12, y=300)
        l4 = Button(self.a, text='<< Main Menu', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=15, padx=10,
                    command=self.main_menu).place(x=12, y=500)

    def add_book_view(self):
        AddBooks.add_book_view(self)

    def add_book(self):
        AddBooks.add_book(self)

    def search_view(self):
        SearchBooks.search_view(self)

    def search_book(self):
        SearchBooks.search_book(self)

    def combo_box(self, event):
        SearchBooks.combo_box(self, event)

    def delete_book_view(self):
        SearchBooks.delete_book_view(self)

    def delete_book(self):
        SearchBooks.delete_book(self)

    def copies_view(self, varr):
        SearchBooks.copies_view(self, varr)

    def add_copies(self):
        SearchBooks.add_copies(self)

    def delete_copies(self):
        SearchBooks.delete_copies(self)

    def list_all_books(self):
        AllBooks.list_all_books(self)

    def students_menu(self):
        self.a.destroy()
        self.a = self.canvases(image2)
        l1 = Button(self.a, text='Issue book', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=15, padx=10,
                    command=self.issue_view).place(x=12, y=100)
        l2 = Button(self.a, text='Return Book', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=15, padx=10,
                    command=self.return_view).place(x=12, y=200)
        l3 = Button(self.a, text='All Activities', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=15, padx=10,
                    command=self.activity_view).place(x=12, y=300)
        l4 = Button(self.a, text='<< Main Menu', font='Papyrus 22 bold', bg='black', fg='#3085b9',
                    activebackground='#3085b9', activeforeground='black', width=15, padx=10,
                    command=self.main_menu).place(x=12, y=600)

    def issue_view(self):
        IssueBook.issue_view(self)

    def issue_book(self):
        IssueBook.issue_book(self)

    def return_view(self):
        ReturnBook.return_view(self)

    def return_book(self):
        ReturnBook.return_book(self)

    def activity_view(self):
        AllActivity.activity_view(self)

    def search_activity(self):
        AllActivity.search_activity(self)

    def search_all_activity(self):
        AllActivity.search_all_activity(self)


# ===================START=======================
def canvases(images, w, h):
    photo = Image.open(images)
    photo1 = photo.resize((w, h), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(photo1)

    canvas = Canvas(root, width='%d' % w, height='%d' % h)
    canvas.grid(row=0, column=0)
    canvas.grid_propagate(0)
    canvas.create_image(0, 0, anchor=NW, image=photo2)
    canvas.image = photo2

    # ===========================BG for login========================================================================
    # rectangle in login
    rect = Canvas(canvas, width='400', height='275', bg='white')
    rect.place(x=489, y=150)

    # ===================================================================================================
    return canvas


root = Tk()
root.title("LOGIN")

"""width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)"""

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
canvas = canvases(image3, w, h)


# ==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("db/credentials.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `login` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, "
        "password TEXT)")
    cursor.execute("SELECT * FROM `login` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `login` (username, password) VALUES('admin', 'password')")
        conn.commit()


def Login(event=None):
    Database()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        # messagebox.showinfo("Error","Please complete the required field!")
        lbl_text.config(text="Please fill the required fields!", fg="red", )
    else:
        cursor.execute("SELECT * FROM `login` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            root.destroy()

            a = Menu()
        else:
            # messagebox.showinfo("Error","Invalid username or password.")
            lbl_text.config(text="Invalid Username or Password", fg="red", )
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


# ==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()

# ==============================FRAMES=========================================
'''Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=BOTTOM, pady=20)'''
# ==============================LABELS=========================================

lbl_title = Label(canvas, text="ADMIN LOGIN", font=('Papyrus', 30, 'bold',), bg='#3085b9', fg='white')
lbl_title.place(x=530, y=170)
lbl_username = Label(canvas, text="Username:", font=('Papyrus', 15, 'bold'), bd=4, bg='white', fg='#3085b9')
lbl_username.place(x=500, y=260)
lbl_password = Label(canvas, text="Password :", font=('Papyrus', 15, 'bold'), bd=3, bg='white', fg='#3085b9')
lbl_password.place(x=500, y=310)
lbl_text = Label(canvas)
lbl_text.place(x=490, y=500)
lbl_text.grid_propagate(0)

# ==============================ENTRY WIDGETS==================================
username = Entry(canvas, textvariable=USERNAME, font=14, bg='black', fg='#3085b9', bd=6)
username.place(x=650, y=260, )
password = Entry(canvas, textvariable=PASSWORD, show="*", font=14, bg='black', fg='#3085b9', bd=6)
password.place(x=650, y=310)

# ==============================BUTTON WIDGETS=================================
btn_login = Button(canvas, text="LOGIN", font='Papyrus 15 bold', width=25, command=Login, bg='black', fg='#3085b9',
                   activebackground='#3085b9', activeforeground='black')
btn_login.place(x=500, y=370)
btn_login.bind('<Return>', Login)
root.mainloop()
