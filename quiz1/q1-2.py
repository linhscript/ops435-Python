#!/usr/bin/env python3

import sys
a1 = int(sys.argv[1] )
a2 = sys.argv[2]
if a1 <= 0:
    print("ValueError: the first argument must be greater than 0")
else:
    print(a1*a2)