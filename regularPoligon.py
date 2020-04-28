class RegularPoligon:

    def __init__(self, crds, ns):
        if ns == 4:
            self.type = 'square'
        elif ns == 6:
            self.type = 'hexagon'
        else:
            print('wrong value of variable "ns"')
        self.coordinates = crds
        angle = 360/ns
        self.awl = {}
        for x in range(1, ns + 1):
            gs = angle * x
            self.awl[int(gs)] = None

    def get_angles(self):
        return self.awl

    def get_cors(self):
        return self.coordinates

    def get_type(self):
        return self.type

    def set_link(self, an, crs):
        self.awl[an] = crs

