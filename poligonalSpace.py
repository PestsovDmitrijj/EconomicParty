from regularPoligon import RegularPoligon

# spatial orientation for hexagons
cfsh = {60: [0, 1, 240], 120: [-1, 1, 300], 180: [-1, 0, 360], 240: [0, -1, 60], 300: [1, -1, 120], 360: [1, 0, 180]}


# creating a relationship with objects
def cc(o1, o2, an):
    o1.set_link(an, o2.get_cors())
    o2.set_link(cfsh[an][2], o1.get_cors())


# create neibhourhoods; parameter object with type RegularPoligon
def cr_nbhs(obj):
    nbhs = []
    step = int(360 / len(obj.get_angles()))
    langle = step

    # creating a few objects around object and connecting center object with periphery
    while langle <= 360:
        if obj.get_angles()[langle] == None:
            # new object of RegularPoligon
            nbhs.append(RegularPoligon([
                obj.get_cors()[0] + cfsh[langle][0],
                obj.get_cors()[1] + cfsh[langle][1],
                obj.get_cors()[2] + 1
            ], 6))
            cc(obj, nbhs[-1], langle)

        #connecting peripherial objects between themselves
        pl = langle - step
        nl = langle + step
        if pl <= 0:
            pl = 360
        elif pl > 360:
            pl = 0

        if nl <= 0:
            nl = 360
        elif nl > 360:
            nl = 0

        nbo = RegularPoligon
        nbt = RegularPoligon
        if obj.get_angles()[pl] != None:
            for x in nbhs:
                if x.get_cors() == obj.get_angles()[pl]:
                    # print(x.get_cors(), '=>', chln)
                    nbo = x
                elif x.get_cors() == obj.get_angles()[langle]:
                    nbt = x
            print(pl, '=>', nbo.get_cors(), 'must be neibhourhoods with', langle, '=>', nbt.get_cors())

        langle += step

    return nbhs
