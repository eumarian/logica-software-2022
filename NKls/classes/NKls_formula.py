from pprint import pprint

class NKlsFormula:

    def __init__(self, subformula1, op='', subformula2=None):
        self.str = ''
        self.op = op
        self.subformula1 = subformula1
        self.subformula2 = subformula2


        if not op:
            self.str = self.subformula1
            self.subformula1 = self.string()


        self.str = self.string_create()

        print(self.str)

    def string_create(self):
        if self.is_atomic():
            ret = self.subformula1
        elif self.op == '~':
            ret = self.op + self.subformula1.string(True)
        else:
            ret = self.subformula1.string(True) + ' ' + self.op + ' ' + self.subformula2.string(True)
        return ret

    def string(self, external_brackets=False):
        ret = self.str
        if not self.is_atomic() and self.op != '~' and external_brackets:
            ret = '(' + ret + ')'

        return ret

    def is_atomic(self):
        return not self.op

    def op(self):
        return self.op

    def subformula1(self):
        return self.subformula1

    def subformula2(self):
        return self.subformula2

    def subformulas(self):
        ret = [self.subformula1, self.op, self.subformula2]
        return ret

    def length(self):
        ret = 0
        if not self.is_atomic():
            l1 = self.subformula1
            l2 = self.subformula2 if self.subformula2 else 0
            ret = max(l1, l2)
        return ret

