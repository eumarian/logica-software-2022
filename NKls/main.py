from classes.NKls_formula import NKlsFormula
from classes.NKls import NKls
from pprint import pprint
#if __name__ == '__main__':

system = NKls()



t =  NKlsFormula('T')
d =  NKlsFormula('D')
c =  NKlsFormula('C')

td  = NKlsFormula(t,'&',d)
dc = NKlsFormula(d,'&',c)
tdc = NKlsFormula(t,'&',dc)
tddc = NKlsFormula(td,'&',dc)

nt =  NKlsFormula(t,'~')



dtd =  NKlsFormula(d,'<->',td)
ndtd =  NKlsFormula(dtd,'&',t)

print("logica si software")
print( t.string() )
print( t.length() )
print( tddc.string() )
print( tddc.length() )




