# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from typing import Iterable

def flatten(xs) -> Iterable[int]:
    for x in xs:
        if x.isInteger(): yield x.getInteger()
        else: yield from flatten(x.getList())

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._it = flatten(nestedList)
        self._next = next(self._it, None)
    
    def next(self) -> int:
        x, self._next = self._next, next(self._it, None)
        return x
    
    def hasNext(self) -> bool:
        return self._next is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())