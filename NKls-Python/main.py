from classes.NKls_formula import NKlsFormula
from classes.NKls import NKls
if __name__ == '__main__':

    system = NKls()

    a = NKlsFormula('A')
    b = NKlsFormula('B')
    c = NKlsFormula('C')
    d = NKlsFormula('D')
    nd = NKlsFormula(d, '~')
    nnd = NKlsFormula(nd, '~')

    ad = NKlsFormula(a, '&', nnd)
    bc = NKlsFormula(b, '&', c)
    abc = NKlsFormula(a, '&', bc)
    abcd = NKlsFormula(abc, '&', ad)


    system.line_add(abcd,'premise')

    system.target_set('d')

    system.run()