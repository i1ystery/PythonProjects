class A:
    def __init__(self):
        self.a_variable = True

    def test(self):
        print('A')


class B:
    def __init__(self):
        self.b_variable = True

    def test(self):
        print('B')


class C(A, B):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        B.__init__(self)


# Experiment 1
c = C()
c.test()
# Experiment 2 & 3
print(c.a_variable, c.b_variable)

