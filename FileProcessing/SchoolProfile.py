class SchoolProfile:
    def __init__(self, name, lastname, username, favorite_school_subject, favorite_school, favorite_teacher):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.favorite_school_subject = favorite_school_subject
        self.favorite_school = favorite_school
        self.favorite_teacher = favorite_teacher

    def __str__(self):
        return f'Name: {self.name} Lastname: {self.lastname}\nUsername: {self.username}\nFavorite school subject: {self.favorite_school_subject}\nFavorite school: {self.favorite_school}\nFavorite teacher: {self.favorite_teacher}'
