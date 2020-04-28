from regularPoligon import RegularPoligon


def get_all_patameters(obj):
    print('output parameters of object')
    print('The type of ', obj.get_type())
    print('Coordinates', obj.get_cors())
    print('Angles of object', obj.get_angles())


o1 = RegularPoligon([0, 0, 0], 6)
o2 = RegularPoligon([0, 1, 1], 6)
o3 = RegularPoligon([0, -1, -1], 6)

print('obj one')
get_all_patameters(o1)
print('obj two')
get_all_patameters(o2)
print('obj three')
get_all_patameters(o3)

print('check set_link function')
o1.set_link(60, o2.get_cors())
o2.set_link(240, o1.get_cors())
print(o1.get_angles())
print(o2.get_angles())
