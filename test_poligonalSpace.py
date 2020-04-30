from poligonalSpace import RegularPoligon, cc, cr_nbhs

print('test function cc')
p1 = RegularPoligon([0, 0, 0], 6)
p2 = RegularPoligon([0, 1, 1], 6)
cc(p1, p2, 60)
print('obj one:', p1.get_angles(), '\nobj two:', p2.get_angles())

print('test function cr_nbhs')
o1 = RegularPoligon([0, 0, 0], 6)
nbhs = cr_nbhs(o1)

print(o1.get_angles())
for x in nbhs:
    print(x.get_angles())
