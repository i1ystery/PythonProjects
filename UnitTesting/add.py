
def add(a,b):
    if type(a or b) not in [int, float, complex]:
        raise TypeError('Muzete scitat jenom int, float, complex')
    return a + b
