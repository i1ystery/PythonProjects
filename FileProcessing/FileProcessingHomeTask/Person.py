class Person:
    def __init__(self, name, lastname, birth_date, job, phone_number):
        self.name = name
        self.lastname = lastname
        self.birth_date = birth_date
        self.job = job
        self.phone_number = phone_number

    def __str__(self):
        return f'Name: {self.name}\nLastname: {self.lastname}\nDate of birth: {self.birth_date}\n' \
               f'Job: {self.job}\nPhone number: {self.phone_number}'

    def get_as_list(self):
        return [self.name, self.lastname, self.birth_date, self.job, self.phone_number]
