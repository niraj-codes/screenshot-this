
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

        
        
