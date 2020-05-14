from poligonalSpace import RegularPoligon, cc, cr_nbhs, cpo_bt, cl_2d, hs2d, print_results, go

o1 = RegularPoligon([0, 0, 0], 4)
nbhs = []
nbhs.append(o1)
nbhs.append(cr_nbhs(o1))
print_results(nbhs)