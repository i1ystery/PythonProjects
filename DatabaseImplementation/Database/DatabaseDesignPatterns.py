from UserDAO import *
if __name__ == '__main__':
    a = UserDAO()
    matej = User(None, 'Matej', 1234, 'Blue')
    a.save(matej)
    print(a.get_all_users())
    a.export_users('export_users.json')
    print(a.get_users_by_username('Matej'))
    dima = User(None, 'Dima', 6853368, 'White')
    print(dima)
    a.save(dima)
    print(a.get_all_users())
    dima.favorite_color = 'Bloody Red'
    a.save(dima)
    print(a.get_all_users())
    a.delete_user(dima)
    print(a.get_all_users())
    a.import_users('insert.csv')
    print(a.get_all_users())
