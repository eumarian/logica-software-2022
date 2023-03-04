from .NKls_rule import NKlsRule
from .NKls_line import NKlsLine
from .NKls_rule_conj_elim import NKls_rule_conj_elim
from .NKls_rule_neg_elim import NKls_rule_neg_elim
from .NKls_rule_impl_intr import NKls_rule_impl_intr
from .NKls_rule_neg_intr import NKls_rule_neg_intr
from .NKls_rule_conj_intr import NKls_rule_conj_intr
from .NKls_rule_disj_elim import NKls_rule_disj_elim
from .NKls_rule_disj_intr import NKls_rule_disj_intr
from .NKls_rule_impl_elim import NKls_rule_impl_elim
from .NKls_rule_equiv_intr import NKls_rule_equiv_intr
from .NKls_rule_equiv_elim import NKls_rule_equiv_elim
from .NKls_rule_seq_dn import NKls_rule_seq_dn
import numpy as np


class NKls:

    def __init__(self):
        self.lines = self.lines_success = self.rules = []
        self.target = False
        self.rules_add()

    staticmethod
    def lines_length(lines):
        ret = 0
        for line in lines:
            l = 15 # DACA EXISTA METODA ?????
            if l > ret:
                ret = l

        return ret

    def rules_add(self):
        for key, op in NKlsRule.ops.items():
            classe = 'NKls_rule_' + op['short'] + '_elim'
            classi = 'NKls_rule_' + op['short'] + '_intr'
            self.rules.append(eval(classe))
            self.rules.append(eval(classi))
        for key, seq in NKlsRule.seqs.items():
            classeq = 'NKls_rule_seq_' + seq['short']
            self.rules.append(eval(classeq))

            print(self.rules)


    def premises_base_lines(self):
        ret = []
        for line in self.lines:
            if line.source_type == 'premise':
                ret = np.unique(np.array(ret + line.base_lines()))


    def compute_lines_success(self, newline):
        log = {newline.line_number(): newline}
        sort = {newline.line_number(): newline.line_number()}

        source_lines = newline.source_lines

        while True:
            breakLoop = True
            for no in source_lines:
                if log.has_key(no):
                    anotherline = self.lines[no]
                    log[no] = anotherline
                    sort[no] = no
                    source_lines = source_lines + anotherline.source_lines
                    breakLoop = False

            if breakLoop:
                break

        ## multisort ????????????

        self.lines_success = log

    def run(self):
        error = False
        if not self.target:
            error = 'no target'
        if not error and not self.lines:
            error = 'no lines'

        emptypasses_limit = 1
        passlog = {}
        emptypasses = passes = 0


        print(self.rules)
        # maxl = NKls.lines_length(self.lines + self.target)
        maxl = 4

        already_strings = []

        while True:
            # lines_no = len(self.lines)

            for attr, value in vars(self.lines).items():
                print(attr, '=', value)


    def target_set(self, target):
        self.target = target

    def line_find(self, string):
        ret = False
        for line in self.lines:
            if string == line.line_formula():
                ret = line
                break

        return ret

    def rule_get(self, short):
        ret = False
        for rule in self.rules:
            if rule.op_short() == short:
                ret = rule
        return ret



    def line_add(self, formula, source_type, base_lines=[], source_rule='', source_lines=[]):
        ret = NKlsLine(self, formula, source_type, base_lines, source_rule, source_lines)
        return ret


