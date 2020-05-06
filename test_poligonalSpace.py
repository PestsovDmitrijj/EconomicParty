from poligonalSpace import RegularPoligon, cc, cr_nbhs, cpo_bt, sni, cl_2d, hs2d

print('test function cc')
p1 = RegularPoligon([0, 0, 0], 6)
p2 = RegularPoligon([0, 1, 1], 6)
cc(p1, p2, 60)
print('obj one:', p1.get_angles(), '\nobj two:', p2.get_angles())


def print_results(lst):
    for x in lst:
        print(x.get_cors(), '=>', x.get_angles())


print('test function cr_nbhs')
o1 = RegularPoligon([0, 0, 0], 6)
nbhs = []
nbhs.append(o1)
nbhs.extend(cr_nbhs(o1))
print_results(nbhs)

print('test function cpo_bt')
cpo_bt(nbhs)
cpo_bt(nbhs)
print_results(nbhs)


print('attempt to reproduce all actions')
cl_2d(nbhs, 1, 7)
print_results(nbhs)

print('selection for control')
control = []
control.append(nbhs[7])
control.append(nbhs[13])
control.append(nbhs[18])
print_results(control)


print('checking how working next step')
cl_2d(nbhs, 7, 19)
print_results(nbhs)

print('selection for control')
control.extend([nbhs[20], nbhs[22], nbhs[35], nbhs[36], nbhs[33]])
print_results(control)

print('test function God2d')
null_array = list()
hs2d(null_array, 5)
print_results(null_array)
