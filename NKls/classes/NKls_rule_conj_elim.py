from .NKls_rule import NKlsRule

class NKls_rule_conj_elim(NKlsRule):

    def process(self, lines = []):
        newstructures = []

        for line in lines:
            if line.formula.op() == '&':
                newstructures.append(
                    {"formula": line.formula.subformula1,
                     "base_lines": line.base_lines(),
                     "source_lines": [line.line_number()],
                     }
                )
                newstructures.append(
                    {"formula": line.formula.subformula2,
                     "base_lines": line.base_lines(),
                     "source_lines": [line.line_number()],
                     }
                )
        return newstructures




