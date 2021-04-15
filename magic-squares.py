#!/bin/python

import math
import os
import random
import re
import sys

known_magic_squares = [
    [[8,1,6],[3,5,7],[4,9,2]],
    [[6,1,8],[7,5,3],[2,9,4]],
    [[4,9,2],[3,5,7],[8,1,6]],
    [[2,9,4],[7,5,3],[6,1,8]],
    [[8,3,4],[1,5,9],[6,7,2]],
    [[4,3,8],[9,5,1],[2,7,6]],
    [[6,7,2],[1,5,9],[8,3,4]],
    [[2,7,6],[9,5,1],[4,3,8]]     
]

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    square_sums = [0] * len(known_magic_squares)
    for index, magic_square in enumerate(known_magic_squares):
        for i in range(len(s)):
            for j in range(len(s[0])):
                cur = s[i][j]
                magic = magic_square[i][j]
                if cur != magic:
                    square_sums[index] += abs(cur - magic)
    return min(square_sums)
                
if __name__ == '__main__':
    fptr = sys.stdout
    s = [[7,6,5],[7,2,8],[5,3,4]]
    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()
