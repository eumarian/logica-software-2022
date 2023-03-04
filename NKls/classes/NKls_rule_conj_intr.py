from .NKls_rule import NKlsRule
from .NKls_line import NKlsLine

class NKls_rule_conj_intr(NKlsRule):

    def process(self, lines=[]):
        pass

    def process_sub(self, line1, line2):
        line1f = '(' + line1.formula +')' if not line1.is_atomic() else line1.formula
        line2f = '(' + line2.formula +')' if not line2.is_atomic() else line2.formula

        newformula = line1f + ' & ' + line2f

        ret = NKlsLine(newformula)
