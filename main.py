from locality import Locality

cd = [1, 1]
bp = ['wood', 'food']
lands = []
lands.append( Locality("Moscow", 100, cd, 100, bp) )
lands.append( Locality("Dubai", 150, cd, 200, bp) )

for count, val in enumerate(lands):
    print(val.get_name())
    print(val.get_cash())


