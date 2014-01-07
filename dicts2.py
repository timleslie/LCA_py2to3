d = {1: 10, 2: 20, 3: 30}

# keys() gives us a list
keys = d.keys()
print keys
assert type(keys) is list

ikeys = d.iterkeys()
print ikeys
# We can iterate over the ikeys (obviously)
for k in ikeys:
    print k

# But unlike xrange (for e.g) we can't do this multiple times
print "start"
for k in ikeys:
    print k
print "stop"

