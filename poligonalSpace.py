from regularPoligon import RegularPoligon
import copy

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

    # creating a few objects around object and connecting center object with periphery
    langle = step
    while langle <= 360:
        if obj.get_angles()[langle] is None:
            # new object of RegularPoligon
            nbhs.append(RegularPoligon([
                obj.get_cors()[0] + cfsh[langle][0],
                obj.get_cors()[1] + cfsh[langle][1],
                obj.get_cors()[2] + 1
            ], 6))
            cc(obj, nbhs[-1], langle)
        langle += step

    result = []
    result.extend(nbhs)
    return result


# connect peripheral objects between themselves
def cpo_bt(lo=list):
    step = int(360 / len(lo[0].get_angles()))
    langle = step
    nbhs = lo[1:len(lo)]
    while langle <= 360:
        nlg = langle + step
        if nlg > 360:
            nlg = 60
        if lo[0].get_angles()[nlg] is not None and lo[0].get_angles()[langle] is not None:
            al = langle + step * 2
            if al > 360:
                al -= 360

            # get neighbours for connecting
            nbo = RegularPoligon
            nbt = RegularPoligon
            for x in nbhs:
                if x.get_cors() == lo[0].get_angles()[langle]:
                    nbo = x
                elif x.get_cors() == lo[0].get_angles()[nlg]:
                    nbt = x

            if nbo.get_angles()[al] == None:
                cc(nbhs[nbhs.index(nbo)], nbhs[nbhs.index(nbt)], al)

        langle += step


# selection for the next iteration
def sni(objects, index):
    obj = objects[index]
    result = []
    result.append(obj)
    for x in obj.get_angles():
        for y in objects:
            if obj.get_angles()[x] == y.get_cors():
                result.append(objects[objects.index(y)])

    return result


# create controller for 2d space; create level in hexaspace
def cl_2d(lst, s, f):
    for i in range(s, f):
        lst.extend(cr_nbhs(lst[i]))
        cpo_bt(sni(lst, i))


# God of 2dHexaSpace
def hs2d(hs, r):
    if len(hs) == 0:
        hs.append(RegularPoligon([0, 0, 0], 6))
        hs.extend(cr_nbhs(hs[0]))
        cpo_bt(hs)

    s = 1
    for i in range(1, r - 1):
        f = len(hs)
        cl_2d(hs, s, f)
        s += i * 6


def print_results(lst):
    for x in lst:
        print(x.get_cors(), '=>', x.get_angles())


# good function for path finding
def go(start, path, space):
    for obj in space:
        if obj.get_cors() == start:
            sp = obj

    for point in path:
        for x in sp.get_angles():
            if sp.get_angles()[x] == point:
                for obj in space:
                    if obj.get_cors() == point:
                        print(sp.get_cors(), '=>', x, ':', sp.get_angles()[x])
                        sp = obj


# copy the space for sphere
def cfs(nsp):
    # sort by z parameter
    z = 0
    sort = []
    sg = []
    for x in nsp:
        if x.get_cors()[2] == z and nsp.index(x) != len(nsp) - 1:
            sg.append(x)
        elif x.get_cors()[2] != z:
            sort.append(copy.deepcopy(sg))
            sg = []
            sg.append(x)
            z += 1
        elif nsp.index(x) == len(nsp) - 1:
            sg.append(x)
            sort.append(copy.deepcopy(sg))

    return sort


#correcting links
def cor_link(space):
    #get equator
    eq = space[len(space) - 1].get_cors()[2] - 1
    for x in space:
        for y in x.get_angles():
            if x.get_angles()[y] is not None:
                if x.get_angles()[y][2] - eq < 0:
                    #different
                    df = (x.get_angles()[y][2] - eq) * -2
                    x.get_angles()[y][2] += df

    return space


#change coordinates of sides in hexagons
def ccsh(space):
    for x in space:
        angle = 60
        for a in range(1, 4):
            aa = angle * a
            #addition value
            av = x.get_angles()[aa]
            x.get_angles()[aa] = x.get_angles()[aa + 180]
            x.get_angles()[aa + 180] = av


#change z coordinate in sorted copy of space
def ccscs(space):
    nsp = copy.deepcopy(space)
    sorted = cfs(nsp)
    #get last coordinate z
    z = sorted[len(sorted) - 1][len(sorted[len(sorted) - 1]) - 1].get_cors()[2] + 1
    #increase z coordinate
    for x in range(1, len(sorted) + 1):
        z += 1
        for y in sorted[-x]:
            y.get_cors()[2] = z

    result = []
    for x in sorted:
        result += x
    result = cor_link(result)
    ccsh(result)

    return result



















