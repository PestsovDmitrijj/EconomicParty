class Locality:

    __nameLoc = ""
    __populate = 0
    __coordinate = { 'x': 0, 'y': 0 }
    __cash = 0
    __base_products = []

    def __init__( self, nameLoc, cp, cd, ca, bp ):

        self.__nameLoc = nameLoc
        self.__populate = cp
        self.__coordinate['x'] = cd[0]
        self.__coordinate['y'] = cd[1]
        self.__cash = ca
        self.__base_products = bp

    def get_name(self):
        return self.__nameLoc

    def get_type(self):
        return 'Locality'

    def get_populate(self):
        return self.__populate

    def get_coordinate(self):
        return self.__coordinate

    def get_cash(self):
        return self.__cash

    def get_base_products(self):
        return self.__base_products
