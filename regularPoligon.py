class RegularPoligon:

    __type = None
    __coordinates = list
    __awl = {}          #angles with links

    #coordinates
    #number of sides
    def __init__(self, crds, ns = int):
        if ns == 4:
            self.__type = 'square'
        elif ns == 6:
            self.__type = 'hexagon'
        else:
            print('wrong value of variable "ns"')
        self.__coordinates = crds
        angle = 360/ns
        for x in range(1, ns + 1):
            gs = angle * x
            self.__awl[int(gs)] = [0, x]

    def get_angles(self):
        return self.__awl

    def get_cors(self):
        return self.__coordinates


