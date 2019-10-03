# A bad implementation of the fibonacci sequence.

def fibonacci(n):
    """
    a very bad implementation for finding the n'th element of the fibonacci sequence.
    """
    #0,1,1,2,3,5,8...

    if n<=0:
        print("ERROR!")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_seq(*args):
    """
    Returns the first n elements using the fibonacci function if given
    only one argument ,or finds a subsequence if given two arguments, I.e.
    fibonacci_seq(n,m) returns [fn, fn+1, fn+2, .. ,fm], and fibonacci_seq(m)
    returns [f1, f2, .. ,fn], where fi is the i'th element of the sequence
    """

    if len(args) == 1:
        return [fibonacci(n) for n in range(1,args[0]+1)]
    elif len(args) == 2:
        return [fibonacci(n) for n in range(args[0], args[1]+1)]
    else:
        print("ERROR!!")
