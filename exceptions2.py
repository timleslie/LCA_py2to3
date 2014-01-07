
## Raising error

try:
    raise "Error"  # Raise a string as an exception? Not since 2.5, sorry.
except Exception as e:
    print "Caught error:", e
    assert str(e) != "Error"

try:
    raise Exception, "Error"  # This is an odd way to do things, but it works in python 2
except Exception as e:
    print "Caught error:", e
    assert str(e) == "Error"

try:
    raise Exception("Error")  # This is how we should do things!
except Exception as e:
    print "Caught error:", e
    assert str(e) == "Error"

## Catching errors
try:
    raise Exception("Error") 
except Exception, e:  # This is one way to assign the exception to a variable
    print "Caught error:", e
    assert str(e) == "Error"

try:
    raise Exception("Error") 
except Exception as e:  # But this is a much better way to do it
    print "Caught error:", e
    assert str(e) == "Error"
