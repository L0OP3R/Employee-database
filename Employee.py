import sqlite3

connection = sqlite3.connect("company.db")
connection.execute(''' CREATE TABLE EMPLOYEE_DATABASE(
                       EMPLOYEE_CODE INTEGER PRIMARY KEY AUTOINCREMENT,
                       NAME TEXT,
                       DESIGNATION TEXT,
                       COMPANYNAME TEXT,
                       SALARY INTEGER,
                       PHONE_NUMBER INTEGER
                       ); ''')
print("Table created")
getName = input("Enter name: ")
getDesignation = input("Enter post: ")
getSalary = input("Enter salary amount: ")
getCompanyName = input("enter company name: ")
getMobile_name = input("enter mobile number: ")
connection.execute("INSERT INTO EMPLOYEE_DATABASE(NAME, DESIGNATION,SALARY,COMPANYNAME,PHONE_NUMBER)VALUES('"+getName+"','"+getDesignation+"',"+getSalary+",'"+getCompanyName+"',"+getMobile_name+")")
connection.commit()
connection.close()
print("Successfull")