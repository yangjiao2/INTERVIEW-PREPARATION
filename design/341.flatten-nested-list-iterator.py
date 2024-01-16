
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = [[nestedList, 0]]

    def next(self) -> int:
        self.hasNext()
        lst, index = self.nestedList[-1]
        self.nestedList[-1][1] += 1
        return lst[index].getInteger()

    def hasNext(self) -> bool:
        nestedList = self.nestedList
        while nestedList:
            lst, index = self.nestedList[-1]

            if index == len(lst):
                nestedList.pop()
            else:
                cur = lst[index]
                if cur.isInteger():
                    return True
                nestedList[-1][1] += 1
                nestedList.append([cur.getList(), 0])

        return False
