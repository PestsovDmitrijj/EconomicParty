from poligonalSpace import RegularPoligon, cc, cr_nbhs, cpo_bt, cl_2d, hs2d, print_results, go, cfs, ccscs, ccsh

print('test function cc')
p1 = RegularPoligon([0, 0, 0], 6)
p2 = RegularPoligon([0, 1, 1], 6)
cc(p1, p2, 60)
print('obj one:', p1.get_angles(), '\nobj two:', p2.get_angles())

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

#test path
tp = [[-1, 1, 1], [-2, 2, 2], [-2, 3, 3], [-2, 4, 4], [-1, 4, 4], [0, 3, 3], [1, 3, 4], [2, 2, 4], [3, 1, 4], [4, 0, 4]]
print('testing path:\n', tp)
go([0, 0, 0], tp, null_array)


print('creating a copy of hexaspace 2d')
copy_array = ccscs(null_array)
print_results(copy_array)


#test path
tp = [[-1, 1, 1], [-2, 2, 2], [-2, 3, 3], [-2, 4, 4], [-1, 4, 4], [0, 3, 3], [1, 3, 4], [2, 2, 4], [3, 1, 4], [4, 0, 4]]
print('testing path:\n', tp)
go([0, 0, 0], tp, null_array)
#test path
tp2 = [[-1, 1, 9], [-2, 2, 8], [-2, 3, 7], [-2, 4, 6], [-1, 4, 6], [0, 3, 7], [1, 3, 6], [2, 2, 6], [3, 1, 6], [4, 0, 6]]
print('testing path in copy:\n', tp2)
go([0, 0, 10], tp2, copy_array)

