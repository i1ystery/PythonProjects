from DBConnection import DBConnection
import csv
import json


class User:
    def __init__(self, id_user, username, fav_number, fav_color):
        assert isinstance(username, str) and len(username) <= 40
        assert isinstance(fav_number, int)
        assert isinstance(fav_color, str) and len(fav_color) <= 40
        self.id_user = id_user
        self.username = username
        self.favorite_number = fav_number
        self.favorite_color = fav_color

    def __str__(self):
        return f'ID: {self.id_user}\nUsername: {self.username}\nFavorite number: {self.favorite_number}\nFavorite_color: {self.favorite_color}'


class UserDAO(object):
    def __init__(self):
        self.conn = DBConnection()
        self.auto_commit = True

    def get_all_users(self):
        return self.conn.execute_query("SELECT * from Users", None).fetchall()

    def get_users_by_username(self, username):
        return self.conn.execute_query("SELECT * from Users where username = ?", username).fetchall()

    def save(self, user: User):
        if user.id_user is None:
            self.conn.execute_command("INSERT INTO Users values (?, ?, ?)", (user.username, user.favorite_number, user.favorite_color),
                                      self.auto_commit)
            user.id_user = self.conn.execute_query('SELECT TOP(1) id_user FROM Users ORDER BY id_user DESC', None).fetchone()[0]
        else:
            self.conn.execute_command("UPDATE Users set username = ?,favorite_number = ?, favorite_color = ? where id_user = ?",
                                      (user.username, user.favorite_number, user.favorite_color, user.id_user), self.auto_commit)

    def delete_user(self, user: User):
        self.conn.execute_command("DELETE FROM Users where id_user = ?", user.id_user, self.auto_commit)

    def import_users(self, path):
        try:
            self.auto_commit = False
            with open(path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    user = User(None, *row)
                    self.save(user)
            self.conn.commit()
            self.auto_commit = True
        except Exception as e:
            print(e)
            self.conn.rollback()
            self.auto_commit = True

    def export_users(self, path):
        export = {
            "Entries": []
        }
        for entry in self.get_all_users():
            export['Entries'].append(
                {
                    'id': entry[0],
                    'username': entry[1],
                    'favorite_number': entry[2],
                    'favorite_color': entry[3]
                }
            )
        with open(path, 'w') as file:
            json.dump(export, file, indent=True)
