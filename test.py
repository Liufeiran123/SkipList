__author__ = 'lfr'

from SkipList import SkipList

sl = SkipList(12)
sl.Insert(5)
print sl.Contains(5)
print sl.Contains(6)
sl.Delete(5)
print sl.Contains(5)