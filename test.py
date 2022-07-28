def func(x):
    pass


class UpSkill:
    def __init__(self, a):
        self.a = a

    def other_meth(self):
        return self.a * 2

    def meth(self):
        return self.other_meth() * 5

x = UpSkill(1)
print('heh')
print(x.meth())