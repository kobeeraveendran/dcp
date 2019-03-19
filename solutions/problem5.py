def cons(a, b):

    def pair(f):
        return f(a, b)

    return pair

# notes: cons takes two ints
# pair takes a function and returns the result of calling that function on the two ints
# cons returns pair

# cons(3, 4) --> f(3, 4)
# car(f(3, 4)) --> 3        : f(a, b) = a
# cdr(f(3, 4)) --> 4        : f(a, b) = b

# in cons(), pair() applies a function f() to variables a and b
# so, if we want to get a, we need to define the function f() that pair() requires
# car will be f in this case, and similarly, cdr will be another f
def car(pair):
    def first(a, b):
        return a

    return pair(first)

def cdr(pair):
    def last(a, b):
        return b
    
    return pair(last)

# test cases
print(car(cons(3, 4)))      # expected output: 3
print(cdr(cons(3, 4)))      # expected output: 4