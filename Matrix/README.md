# Matrix:

4 directions, n = len(matrix), m * n corresponds to r, c range

### initiation:
[[-1 ] * n for _ in range(n)]

### reversal methods:
1. coor = coor + direction
2. for i in xrange(top + 1, bottom)

### stopping condition:
1. assigned value in array / matrix
2. top < bottom, left < right
3. linked list is done (need to add last value for while loop check on head.next != None)