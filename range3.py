"""
In python 3, range() returns an xrange object, rather than a list. An xrange
object behaves like a list in many situations, however there are some cases
where they behave differently. In these cases, calls to range() must be wrapped
in a list() to ensure correct behaviour.
"""

N = 10

range10 = range(N)  # This creates an object which behave a bit like a list, but without the O(N) memory cost

try:
    xrange10 = xrange(N)
except NameError:
    print("xrange() no longer exists in python 3")

# Multiple iterations
for xx in range10:
    print(xx)
for xx in range10:
    print(xx)

# Indexing
print(range10[5])

# len()
print(len(range10))

# slicing works on range() objects! -> returns another range object
print(range10[2:5])

# But append/pop still don't work... need to convert to a list first
try:
    range10.append(11)
except AttributeError as e:
    print("ERROR", e)
    range10_list = list(range10)
    range10_list.append(11)
    print(range10_list.pop())
