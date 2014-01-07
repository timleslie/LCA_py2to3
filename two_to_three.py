"""
Toy program to practice porting from python 2 to python 3
"""

from __future__ import with_statement
import os
import sys
import types
import itertools
from itertools import izip

# We use octal notation here because, you know... octal!
ROWS = 06
COLS = 42 / ROWS  # I really want to make sure we end up with 42 spaces
assert ROWS <> COLS  # Let's make sure we got different numbers

WORDS = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG".split()
WORDS.sort()


SQUARES = [x*x for x in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def word_lengths():
    d = {}
    for word in WORDS:
        d[word] = len(word)
    return d

def all_even_numbers(n):
    return filter(lambda x: x % 2 == 0, range(n))

def tuple_func((a, b), c):
    print "A", a
    print "B", b
    print "C", c

class Board(object):

    def __init__(self):
        print "New game started"

    def player_move(self):
        pass

    def check_player(self):
        pass

    def computer_move(self):
        pass

    def check_computer(self):
        pass


def main(msg):
    if not isinstance(msg, basestring):
        raise TypeError, "I really wanted a basestring :-("

    b = buffer(msg)
    print "BUFFER", b  # Just checking that this works...

    print "Running main:", msg

    print "All the even numbers less than 20:"
    print all_even_numbers(20)

    print type(os.getcwdu()), type(os.getcwd())  # These are different in python 2!

    d = word_lengths()
    # Let's just make sure we have one of our words...
    assert d.has_key("DOG")

    print "WORDS"
    for word in d.keys():
        print word

    print "LENGTHS"
    for length in d.itervalues():
        print length

    # Backticks let us do some cool stuff!
    print `ROWS * COLS`  # Should print the string "42"

    # I'm pretty sure this is all of them... 
    all_primes = set([2, 3, 5, 7, 11, 13])
    print all_primes

    sum_of_primes = reduce(lambda x, y: x + y, all_primes, 0)
    print "The sum of all primes is", sum_of_primes

    # I'm using a big number, I'd better make sure python knows to make it a long!
    big_num = long(100.1)
    print "My, what a big number!", big_num

    z1 = zip([1, 2, 3], [10, 11, 12])
    print z1

    z2 = itertools.izip([1, 2 ,3], [10, 11, 12])
    print z2
    
    board = Board()

    doubles = map(lambda x: 2*x, [1, 2, 3])
    print doubles

    try:
        raise
    except:
        a, b, c = sys.exc_value, sys.exc_type, sys.exc_traceback
        print a
        print b
        print c

    print isinstance(10, (int, int))  # Why would you do this? Well, it can be fixed up

    print types.LongType

    try:
        raise StandardError("Woohoo!")
    except StandardError as e:
        print e

    tuple_func((1, 2), 3)

    for line in open("connect4.py").xreadlines():
        print line,

    while 1:
        board.player_move()
        board.check_player()
        board.computer_move()
        board.check_computer()
        break

if __name__ == '__main__':
    print "New game with", ROWS, "rows and", COLS, "cols"

    if not callable(main):  # This will need to be changed in python 3.0/3.1 but comes back in 3.2+
        raise Exception("We're going to have a problem here...")

    try:
        apply(main, ("Hello world",))  # Why do things the easy way?
    except TypeError, e:
        print "Oh dear, I got an error"
        print e
        raise
