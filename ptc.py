import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the 'sockMerchant' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
def sockMerchant(n, ar):
    # Write your code here
    c = 0
    for i in [len(list(g)) for k, g in groupby(sorted(ar))]:
        c += int(i/2) 
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
