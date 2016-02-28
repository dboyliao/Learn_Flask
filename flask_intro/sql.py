import sqlite3

with sqlite3.connect("sample.db") as sampleDB:
    cursor = sampleDB.cursor()
    try:
        cursor.execute("""DROP TABLE posts""")
    except:
        cursor.execute("CREATE TABLE posts(titile TEXT, description TEXT)")
        cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
        cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')