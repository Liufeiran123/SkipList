__author__ = 'lfr'

import random
import sys

class SkipList:
    def __init__(self,height,Comparator):
        self.kMaxHeight = height
        self.cmpobj = Comparator
        self.SkipListData = []
        for i in range(self.kMaxHeight):
            self.SkipListData.append([(None,0)])   #Node(key,indexof(level-1))  -1 tail node

    def Insert(self,Key):
        level = self.GetLevel();

        for k in self.SkipListData[0]:
            if self.cmpobj(Key, k[0]) == 1:
                return

        index = 0
        for l in range(level):
            for i,k in enumerate(self.SkipListData[l]):
                if self.cmpobj(Key,k[0]) == 0:
                    self.SkipListData[l].insert(i+1,(Key,index))
                    index  = i+1;
                    break;

    def Contains(self,Key):
        index = 0
        for level in range(self.kMaxHeight)[::-1]:
            for k in self.SkipListData[level][index:]:
                if self.cmpobj(Key,k[0])==1:
                    return True
            for k in self.SkipListData[level][index:]:
                if self.cmpobj(Key, k[0])==0:
                    index = k[1]
                    break;
                return False
        return False

    def Delete(self,Key):
        for levellist in self.SkipListData:
            for tu in levellist:
                if self.cmpobj(tu[0], Key) == 1:
                    levellist.remove(tu)
                    break;

    def GetLevel(self):
        return random.randint(1,self.kMaxHeight)





