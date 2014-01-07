d = {1: 10, 2: 20, 3: 30}

# keys() gives us a dict_keys object
keys = d.keys()
print(keys)
print(type(keys))
assert type(keys) != list

# We can iterate over the keys
for k in keys:
    print(k)

# We can actuall do this multiple times, much like range()
print("start")
for k in keys:
    print(k)
print("stop")