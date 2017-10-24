# Problem Statement:

# Suppose there are 2 disjoint sets each of size n, representing men=m and women=w.
# The problem is to fine a stable marriage between each m and each w between the two sets.
# However, Each m and w has an associated prefrence list for their respective matching.
# A blocking pair is when there is a preference problem with the current matching.
# Matchings with blocking pairs are known as unstable, otherwise they are stable.

import numpy as np

# x,y are the 2 disjoint sets (arrays)
def stable_marriage(x, y):
	for i in len(x):
		for w in y:


