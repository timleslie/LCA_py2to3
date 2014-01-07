# This is no longer a valid say to spell "not equals"
print 10 <> 20

# This is no longer a valid way to spell "evaluate and return a eval()able string"
print `10 * 20`

# This will do floating point division, rather than integer division
print 21 / 10

# apply() is no longer a thing. Just call the function!
print apply(sum, ([1, 2, 3],))

# buffer() is no longer a thing. It's complicated(tm)
print buffer("123")

# We now use the more pythonic "in" operator
print {1: "a", 2: "b", 3: "c"}.has_key(1)

# reduct() has been demoted from a builtin to the functools module
print reduce(lambda a,b: a + b, [1, 2, 3], 0)
