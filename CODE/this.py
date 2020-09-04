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
        cursor.execute("INSERT INTO `login` (username, password) VALUES('x', 'x')")
        conn.commit()

