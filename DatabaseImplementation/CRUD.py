import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PC398;DATABASE=PV_Users;UID=app1user;PWD=student')
cursor = conn.cursor()
cursor.execute('Select * from Users')


def print_cursor():
    for i in cursor:
        print(i)


def select_by_username(username:str):
    assert isinstance(username, str) and len(username) <= 40
    cursor.execute(f'''Select * from Users where username = '{username}' ''')
    print_cursor()


def select_all():
    cursor.execute(f'''Select * from Users''')
    print_cursor()


def create_user(username: str, favorite_number: int, favorite_color: str):
    assert isinstance(username, str) and len(username) <= 40
    assert isinstance(favorite_number, int)
    assert isinstance(favorite_color, str) and len(favorite_color) <= 40
    cursor.execute(f'''Insert into Users values ('{username}', '{favorite_number}', '{favorite_color}')''')
    cursor.commit()


def update_user_fav_color(username: str, favorite_color: str):
    assert isinstance(username, str) and len(username) <= 40
    assert isinstance(favorite_color, str) and len(favorite_color) <= 40
    cursor.execute(f'''Update Users set favorite_color = '{favorite_color}' where username = '{username}' ''')


def delete_user(username: str):
    assert isinstance(username, str) and len(username) <= 40
    cursor.execute(f'''Delete from Users where username = '{username}' ''')


create_user('Matej', 12, 'Blue')
select_all()
select_by_username('Matej')
update_user_fav_color('Matej', 'Blue')
select_all()
delete_user('Matej')
select_all()
