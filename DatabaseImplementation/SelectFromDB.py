import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PC398;DATABASE=PV_Users;UID=app1user;PWD=student')
cursor = conn.cursor()
cursor.execute('Select * from Users')
for i in cursor:
    print(i)
