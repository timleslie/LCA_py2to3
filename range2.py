"""
In python 3, range() returns an xrange object, rather than a list. An xrange
object behaves like a list in many situations, however there are some cases
where they behave differently. In these cases, calls to range() must be wrapped
in a list() to ensure correct behaviour.
"""

from __future__ import print_function

N = 10

range10 = range(N)  # This creates an actual list of N numbers in memory
xrange10 = xrange(N)  # This creates an object which behave a bit like a list, but without the O(N) memory cost

# Multiple iterations
for xx in range10:
    print(xx)
for xx in range10:
    print(xx)

for yy in xrange10:
    print(yy)
for yy in xrange10:
    print(yy)

# Indexing
print(range10[5])
print(xrange10[5])

# length
print(len(range10))
print(len(xrange10))

# Slicing is one area where xrange is not so great :-(
print(range10[2:5])
try:
    print(xrange10[2:5])  # This will fail. We cannot slice an xrange() object
except TypeError as e:
    print("ERROR", e)
    print(list(xrange10)[2:5])


# append/pop
range10.append(11)
print(range10.pop())

try:
    xrange10.append(11)
except AttributeError as e:
    print("ERROR", e)
    xrange10_list = list(xrange10)
    xrange10_list.append(11)
    print(xrange10_list.pop())

