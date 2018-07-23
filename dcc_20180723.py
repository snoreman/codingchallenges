"""
cons(a, b) constructs a pair and car(pair)
and cdr(pair) returns the first and last element
of that pair
for example, car(cons(3,4)) returns 3
and cdr(cons(3,4)) returns 4

given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

implement car and cdr
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def cdr(pair):
    return pair(lambda a, b: b )


def car(pair):
    return pair(lambda a, b: a )

print(cons(1, 2))
print (cdr(cons(3,4)))
print (car(cons(3,4)))
f = cons(1, 2)

def myfunc(a,b):
    return a

print (f(myfunc))
