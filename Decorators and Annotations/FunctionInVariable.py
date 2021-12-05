# 10.1
# def append_jecna_postfix(username):
#     assert type(username) == str
#     return username + '@spsejecna.cz'
#
# def append_seznam_postfix(username):
#     assert type(username) == str
#     return username + '@seznam.cz'
#
# appender_postfix = append_jecna_postfix
# print(appender_postfix("novak"))
# appender_postfix = append_seznam_postfix
# print(appender_postfix("novak"))


# 10.2
# def create_email(appender_function, username):
#     return appender_function(username)
#
# appender_postfix = append_jecna_postfix
# print(create_email(appender_postfix, "novak"))
# #ma vratit novak@spsejecna.cz
# appender_postfix = append_seznam_postfix
# print(create_email(appender_postfix, "novak"))
# #ma vratit novak@seznam.cz
#
#
# 10.3
# def formatuj_prijmeni_prvni(name, lastname):
#     assert type(name) == str and type(lastname) == str
#     assert len(name) > 0 and len(lastname) > 0
#     return lastname + " " + name
#
#
# def formatuj_monogram(name, lastname):
#     assert type(name) == str and type(lastname) == str
#     assert len(name) > 0 and len(lastname) > 0
#     return name[0] + '.' + lastname[0] + '.'
#
#
# def vyber_formatovaci_funkci(delka):
#     assert type(delka) == int
#     if delka < 4:
#         return formatuj_monogram
#     else:
#         return formatuj_prijmeni_prvni
#
# formatovac = vyber_formatovaci_funkci(3)
# print(formatovac('Jan', 'Novak'))
#
# formatovac = vyber_formatovaci_funkci(155)
# print(formatovac("Jan", "Novak"))

# 10.4

# import random
#
# funky_functions = []
#
#
# def Upper(text: str):
#     return text.upper()
#
#
# funky_functions.append(Upper)
#
#
# def SmileyFace(text: str):
#     return text.replace(' ', ':)')
#
#
# funky_functions.append(SmileyFace)
#
#
# def VtoW(text: str):
#     return text.replace('V', 'W')
#
#
# funky_functions.append(VtoW)
#
#
# def Asterisk(text: str):
#     return '*' + text + '*'
#
#
# funky_functions.append(Asterisk)
#
#
# def ExclamationQuestion(text: str):
#     text = text.replace('?', '???')
#     text = text.replace('!', '!!!!!')
#     return text
#
#
# funky_functions.append(ExclamationQuestion)
#
#
# def funky_format(text: str):
#     for i in range(3):
#         rng = random.randint(0, len(funky_functions) - 1)
#         text = funky_functions[rng](text)
#     return text
#
#
# print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))

# 10.5
#
# def generate_multiply_func(multiply_num: int):
#     def multiply(number):
#         return number * multiply_num
#     return multiply
#
#
# multiply_0 = generate_multiply_func(0)
# multiply_1 = generate_multiply_func(1)
# multiply_negative_1 = generate_multiply_func(-1)
# multiply_17 = generate_multiply_func(17)
# multiply_919 = generate_multiply_func(919)
#
#
# print(multiply_0(24))
# print(multiply_1(22))
# print(multiply_negative_1(121))
# print(multiply_17(2))
# print(multiply_919(3))

# 10.6
# def wrapper_velka_pismena(f):
#     def formatuj_velka_pismena(jmeno, prijmeni):
#         vysledek = f(jmeno, prijmeni)
#         return vysledek.upper()
#     return formatuj_velka_pismena
#
#
# @wrapper_velka_pismena
# def formatuj_cele_jmeno(jmeno, prijmeni):
#     return jmeno + " " + prijmeni
#
# @wrapper_velka_pismena
# def formatuj_zkracene_jmeno(jmeno, prijmeni):
#     return jmeno[0] + ". " + prijmeni
#
#
#
#
# cele_jmeno_velkymi = wrapper_velka_pismena(formatuj_cele_jmeno)
# print (cele_jmeno_velkymi("jan", "novak"))
# zkrace_velkymi = wrapper_velka_pismena(formatuj_zkracene_jmeno)
# print (zkrace_velkymi("jan", "novak"))
#
#
# print(formatuj_cele_jmeno("jan", "novak"))
# # vypise JAN NOVAK
#
# print(formatuj_zkracene_jmeno("jan", "novak"))
# # vypise J. NOVAK

# 10.8

# def wrapper_repeat(f):
#     def twice():
#         f()
#         f()
#     return twice
#
# @wrapper_repeat
# def hellowordl():
#     print("hello world")
#
#
# hellowordl()

10.9

import time


def elapsed_time(f):
    def timer():
        start_time = time.time()
        f()
        end_time = time.time()
        print("Vypocet trval " + str((end_time-start_time)) + " sec")
    return timer

@elapsed_time
def tri_na_sedm_milionu():
    return 3 ** 7000000


tri_na_sedm_milionu()