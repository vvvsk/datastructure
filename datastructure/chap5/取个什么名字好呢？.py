# 八皇后问题
from itertools import *
cols = range(8)
for vec in permutations(cols):
    # permutation(cols)对其全排列
    if (8 == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print(vec)
