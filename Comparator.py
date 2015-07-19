__author__ = 'lfr'

class Comparator:
    def __init__(self):
        pass
    def __call__(self,key1,key2):   #0 >,1 =,2 <
        if key1 > key2:
            return 0;      #
        elif key1 == key2:
            return 1
        else:
            return 2
