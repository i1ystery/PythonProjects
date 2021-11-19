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
def formatuj_prijmeni_prvni(name, lastname):
    assert type(name) == str and type(lastname) == str
    assert len(name) > 0 and len(lastname) > 0
    return lastname + " " + name


def formatuj_monogram(name, lastname):
    assert type(name) == str and type(lastname) == str
    assert len(name) > 0 and len(lastname) > 0
    return name[0] + '.' + lastname[0] + '.'


def vyber_formatovaci_funkci(delka):
    assert type(delka) == int
    if delka < 4:
        return formatuj_monogram
    else:
        return formatuj_prijmeni_prvni

formatovac = vyber_formatovaci_funkci(3)
print(formatovac('Jan', 'Novak'))

formatovac = vyber_formatovaci_funkci(155)
print(formatovac("Jan", "Novak"))

