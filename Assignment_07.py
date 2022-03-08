import sqlite3

connection = sqlite3.connect("college.db")
connection.execute('''CREATE TABLE STUDENT(
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       NAME TEXT,
                       ROLLNUMBER INTEGER,
                       ADMNO INTEGER,
                       COLLEGE TEXT

    );       ''')
print("Table created succesfully")
getName = input("Enter name: ")
getRollNumber = input("Enter Roll Number: ")
getADmno = input("ENTER ADMNO : ")
getCollege = input("Enter college name: ")
connection.execute("INSERT INTO STUDENT(NAME , ROLLNUMBER,ADMNO , COLLEGE) VALUES('"+getName+"',"+getRollNumber+","+getADmno+",'"+getCollege+"')")
connection.commit()
connection.close()
print("INSERTED")
