import re


def password_policy_check(username, password):
    assert re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)(?!.*\n)\S{10,}$', password)
    split_list = []
    for i in range(len(username)):
        for j in range(i + 3, len(username) + 1):
            split_list.append(username[i:j])
    for x in split_list:
        assert re.search(x, password, flags=re.IGNORECASE) is None
    print('Your password is safe')


password_policy_check('Max', 'aasdAsdasd2@')