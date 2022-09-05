import sqlite3

conn = sqlite3.connect('fichero.db')
cursor = conn.cursor()

table = cursor.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    first_name CHAR(50) NOT NULL,
    last_name CHAR(50) NOT NULL);""")

cursor.close()
conn.close()


def main():
    insert_student(9, "Maria", "Agustina")
    insert_student(2, "Juan", "Dominguez")
    insert_student(3, "Pepe", "Bonaparte")
    insert_student(4, "Virginia", "Castillejos")
    insert_student(5, "Julian", "Alvarez")
    insert_student(6, "Marcelo", "Gallardo")
    insert_student(7, "Dario", "Benedetto")
    insert_student(8, "Agustin", "Acosta")

    select_student(5)


def insert_student(id, first_name, last_name):
    conn2 = sqlite3.connect('fichero.db')
    cursor2 = conn2.cursor()

    query = ''' INSERT INTO students (id, first_name, last_name) VALUES (?, ?, ?)'''

    rows = cursor2.execute(query, (id, first_name, last_name))
    conn2.commit()
    cursor2.close()
    conn2.close()


def select_student(id):
    conn3 = sqlite3.connect('fichero.db')
    cursor3 = conn3.cursor()

    query = f"SELECT * FROM students WHERE id = {id}"

    rows = cursor3.execute(query)
    data = rows.fetchone()
    print(data)
    cursor3.close()
    conn3.close()


if __name__ == '__main__':
    main()






