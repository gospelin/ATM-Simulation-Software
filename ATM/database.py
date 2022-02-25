import sqlite3

def main():
    conn = sqlite3.connect('Users.db')

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Users (UserID INTEGER PRIMARY KEY NOT NULL, UserName TEXT, Password INTEGER)""")
    cur.execute("""INSERT INTO Users(UserName, Password) VALUES ("Gospel Isaac", 1997)""")

    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()
