from locality import Locality
from hexagon import Hexagon

cd = [1, 1]
bp = ['wood', 'food']
lands = []
lands.append( Locality("Moscow", 100, cd, 100, bp) )
lands.append( Locality("Dubai", 150, cd, 200, bp) )

for count, val in enumerate(lands):
    print(val.get_name())
    print(val.get_cash())


obj1 = Hexagon(0,0)
obj2 = Hexagon(1,0)
obj3 = Hexagon(1,1)

obj1.add_nc( obj2.get_c() )
obj1.add_nc( obj2.get_c() )
print( str( obj1.get_c() ) + " -> " + str( obj1.get_nhds() ) )
print(obj1.get_nhds().index(obj2.get_c()))

print("1")
print(obj1.get_nhds())
mylist = list(dict.fromkeys(obj1.get_nhds()))
print("2")
print(mylist)
