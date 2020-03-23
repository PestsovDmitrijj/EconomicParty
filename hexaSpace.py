from hexagon import Hexagon

hexSpace = list

#create connection
def cc(obj1: Hexagon, obj2: Hexagon):
        obj1.add_nc( obj2.get_c() )
        obj2.add_nc( obj1.get_c() )


def God( circles: int ):
    world = []
    lt = 0          #latitude
    while lt < circles:
        ln = 0
        if lt == 0:
            world.append(Hexagon(lt, ln))
        lt += 1
        sei = len(world) - lt*6 + 1         #senior element index
        if sei < 0:
            print(sei)
            sei = 0
        print(len(world))
        world.append(Hexagon(lt, ln))
        fei = len(world) - 1                #first element index in circle
        cc(world[sei], world[fei])
        for ln in range(1, lt*6-1):
            world.append(Hexagon(lt, ln))

    return world

hexSpace = God(3)

#print("result")
for count, val in enumerate(hexSpace):
    print( str( val.get_c() ) + " -> \t" + str( val.get_nhds() ) )