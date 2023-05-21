#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countshapes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY image as parameter.
#

def countshapes(image):
    res = 0
    board = []
    for line in image:
        board.append(list(line))

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # use dfs to traverse and mark the visited cell back to space (empty cell)
    m, n = len(board), len(board[0])
    def dfs(r, c, board):
        for d in dirs:
            dx, dy = d[0], d[1]
            nr, nc = r+dx, c+dy
            # mark board as visited
            board[r][c] = ' '
            if (0<=nr<m and 0<=nc<n and board[nr][nc] != ' '):
                dfs(nr, nc, board)

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != ' ':
                res += 1
                # traverse the board if we found a non-empty cell
                dfs(r, c, board)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    image_count = int(input().strip())

    image = []

    for _ in range(image_count):
        image_item = input()
        image.append(image_item)

    result = countshapes(image)

    fptr.write(str(result) + '\n')

    fptr.close()
