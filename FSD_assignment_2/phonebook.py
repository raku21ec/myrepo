import sqlite3
try:
    conn = sqlite3.connect("records.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE user3 (id INTEGER, name TEXT, cell BIGINT, email TEXT)")
    cur.execute("""INSERT INTO user3 VALUES (1, 'Randheer', 9353280522, 'raku21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user3 VALUES (2, 'Keerthan', 9353280599, 'keerthan21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user3 VALUES (3, 'Raj', 9353280599, 'raj21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user3 VALUES (4, 'Sagar', 9153280522, 'sagar21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user3 VALUES (5, 'Praneeth', 9334280522, 'praneeth21ec@cmrit.ac.in')""")
    conn.commit()
    print("Insert operation done")

    data=cur.execute("""SELECT * FROM user3""") 
    for row in data: 
        print(row)

except sqlite3.Error as e:
    print("Error while inserting Data", e)

finally:
    if(conn):
        conn.close()
        print("Connection closed")
