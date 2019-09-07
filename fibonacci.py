def fibonacci(n):
    """a very bad implementation for finding the n'th element of the fibonacci sequence."""
    if n==0:
        print("ULAN xd")
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_seq(*args):
    """finds a subsequence of the fibonacci sequence using the fibonacci function"""
    if len(args) == 1:
        return [fibonacci(n) for n in range(1,args[0]+1)]
    elif len(args) == 2:
        return [fibonacci(n) for n in range(args[0], args[1]+1)]
    else:
        print("ulan")
