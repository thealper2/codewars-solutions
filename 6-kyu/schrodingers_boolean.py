class Omnibool:
    def __eq__(self, other):
        return isinstance(other, bool)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __bool__(self):
        return True
    def __hash__(self):
        return hash(True)
    
omnibool = Omnibool()