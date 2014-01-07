import sys

print("Hello world")

print("Hello numbers", 1, 2, 3)

print("Hello %s %s" % ("string", "formatting"))

print("Hello", end=" ")
print("world")

print("Hello stderr", file=sys.stderr)

# Extra stuff!

print("Hello", "world", sep=" ")

print("Hello", "world", end="...\n")