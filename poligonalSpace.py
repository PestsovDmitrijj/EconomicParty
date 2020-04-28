from regularPoligon import RegularPoligon

hexSpace = []

# hexSpace.append(RegularPoligon(crs, 6))

# spatial orientation for hexagons
cfsh = {60: [0, 1, 240], 120: [-1, 1, 300], 180: [-1, 0, 360], 240: [0, -1, 60], 300: [1, -1, 120], 360: [1, 0, 180]}


# creating a relationship with objects
def cc(o1, o2, an):
    o1.set_link(an, o2.get_cors())
    o2.set_link(cfsh[an][2], o1.get_cors())

print('test function cc')
p1 = RegularPoligon([0, 0, 0], 6)
p2 = RegularPoligon([0, 1, 1], 6)
cc(p1, p2, 60)
print('obj one:', p1.get_angles(), '\nobj two:', p2.get_angles())


# create neibhourhoods; parameter object with type RegularPoligon
def cr_nbhs(o):
    nbhs = []
    langle = 60
    while langle <= 360:
        if o.get_angles()[langle] == None:
            # new object of RegularPoligon
            no = RegularPoligon([
                o.get_cors()[0] + cfsh[langle][0],
                o.get_cors()[1] + cfsh[langle][1],
                o.get_cors()[2] + 1
            ], 6)
            # print('Class of type', no.get_type(), 'has coordinates', no.get_cors())

        langle += 60


if hexSpace.__len__() == 0:
    crs = [0, 0, 0]
    hexSpace.append(RegularPoligon(crs, 6))
else:
    while angle <= 360:
        if hexSpace[0].get_angles()[angle] == None:
            print('it is working')

            # hexSpace.append(RegularPoligon())

        hexSpace[0].set_link(angle, angle + 1)
        print(hexSpace[0].get_angles()[angle])
        angle += 60
    print(hexSpace[0].get_angles())

print('test function')

cr_nbhs(hexSpace[0])

print('end_code')
# so, I want to create a function
