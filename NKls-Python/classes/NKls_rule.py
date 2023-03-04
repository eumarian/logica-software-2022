from abc import ABC, abstractmethod


class NKlsRule:
    ops = {"~": {"key": '~', 'short': 'neg', 'name': 'negation', 'binary': False, 'lng': 'not'},
                "&": {"key": '~', 'short': 'conj', 'name': 'conjunction', 'binary': True, 'lng': 'and'},
                "V": {"key": '~', 'short': 'disj', 'name': 'disjunction', 'binary': True, 'lng': 'or'},
                "->": {"key": '~', 'short': 'impl', 'name': 'implication', 'binary': True, 'lng': 'implies'},
                "<->": {"key": '~', 'short': 'equiv', 'name': 'equivalence', 'binary': True, 'lng': 'just in case'}
                }
    seqs = {"dn": {"key": 'dn', 'short': 'dn', 'name': 'DN'}}
    def __init__(self, system):
        self.system = system


    def op_by_short(self, short):
        ret = False
        for key, value in self.ops.items():
            if value['short'] == short:
                ret = value
                break
        return ret

    def seq_by_short(self, short):
        ret = False
        for key, value in self.seqs.items():
            if value['short'] == short:
                ret = value
                break
        return ret

    def op(self):
        ret = False
        cs = ['a','b','c','d'] # DE VAZUT CUM SE FACE get_called_class
        if len(cs) == 4:
            ret = self.op_by_short(cs[3])
        return ret

    def seq(self):
        ret = False
        cs = ['a', 'b', 'c', 'd']  # DE VAZUT CUM SE FACE get_called_class
        if len(cs) == 4:
            ret = self.seq_by_short(cs[3])
        return ret

    def rule_short(self):
        ret = False
        op = self.op()
        seq = self.seq()
        if op:
            ret = 'E' + op['key'] if self.is_elim() else 'I' + op['key']
        elif seq:
            ret = seq['name']

        return ret

    def op_type(self):
        cs = ['a', 'b', 'c', 'd']  # DE VAZUT CUM SE FACE get_called_class
        if len(cs) == 4:
            ret = cs[3]
        return ret

    def is_elim(self):
        return self.op_type() == 'elim'

    def is_introd(self):
        return self.op_type() == 'intr'

    @abstractmethod
    def process(self):
        pass

