import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PC398;DATABASE=PV_Users;UID=app1user;PWD=student')
cursor = conn.cursor()
cursor.execute('''INSERT INTO Users (username, favorite_number, favorite_color) VALUES ('Kokot',1,'cupapi')''')
cursor.commit()
for i in cursor:
    print(i)
