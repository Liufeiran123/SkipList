__author__ = 'lfr'

from SkipList import SkipList
from Comparator import  Comparator

c = Comparator()
sl = SkipList(12,c)
sl.Insert(5)
print sl.Contains(5)
print sl.Contains(6)
sl.Delete(5)
print sl.Contains(5)