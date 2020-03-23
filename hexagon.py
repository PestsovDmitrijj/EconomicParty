class Hexagon:

    __type = "Hexagon"
    __coordinates = list
    __nhds = list

    def __init__(self, lt, ln):
        self.__coordinates = [lt, ln]
        self.__nhds = []

    def get_type(self):
        return self.__type

    def get_c(self):
        return self.__coordinates

    def get_nhds(self):
        return self.__nhds

    def add_nc(self, coords):
        self.__nhds.append(coords)





'''
def God( circles: int ):
    world = []
    lt = 0
    while ( lt < circles ):
        ln = 0
        cln = lt * 6
        if cln == 0:
            world.append( Hexagon(lt, ln) )
            lt += 1
            lcln = 0
            print("first elem")
            print(world[0].get_c())
        else:
            step = cln/6
            for ln in range(0, cln):
                print(str(lcln) + " " + str(lt) + " " + str(ln))
                world.append(Hexagon(lt, ln))
                cc(world[len(world)-1], world[lcln])
                if ln != 0:
                    cc(world[len(world)-1], world[len(world)-2])
                    if ln < cln - 1:
                        if ln % step != 0:
                            lcln += 1
                            cc(world[len(world) - 1], world[lcln])
                            print("polar")
                    else:
                        fs = lcln-6
                        if fs < 0:
                            fs = 0
                        print("I calling" + str(len(world) - 1) + " " + str(fs) + " " + str(fs-1))
                        cc(world[len(world) - 1], world[fs])
                        cc(world[len(world) - 1], world[fs-1])
            #    print( str( world[lcln].get_c() ) + " -> " + str( world[lcln].get_nhds() ) )
            lcln += 1
            lt += 1
            print("end iteration")

    return world
    
    another variant
    
     for lt in range(0, circles):        #lt is latitude
        cln = lt * 6                    #count elements in new circle
        if lt == 0:
            world.append(Hexagon(lt, 0))
            sei = 0                     #start element index
        for ln in range(0, cln):        #ln is longitude
            world.append(Hexagon(lt, ln))
            p = sei                     #pointer: last circle element for connection
            cc( world[len(world) - 1], world[p] )
#            print( str( world[len(world)-1].get_c() ) )     #debug string
            if ln == 0:
                fei = len(world) - 1    #first element index in circle
            elif ln < cln - 1:
                cc(world[len(world) - 1], world[len(world) - 2])
                if ln % lt != 0:
                    p += 1
                    cc(world[len(world) - 1], world[p])
            else:
                sei = fei


    
'''
