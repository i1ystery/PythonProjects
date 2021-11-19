def druha_mocnina(value):
    assert type(value) == int
    return value * value

print(druha_mocnina(3))

x = druha_mocnina

print(x(3))

y = x

print(y(3))