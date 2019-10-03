import itertools

def second_order(p, q, r, initial_values):
    """
    Fibonacci numbers follow a homogeneous linear 
    recurrence relation with constant coefficients
    Fn = Fn-1 + Fn-2
    https://en.wikipedia.org/wiki/Recurrence_relation
    with a solution defined by 
    s(n) = p * s(n-1) + q * s(n-2) + r.
    where p, q and r are constants. 
    To Fibonacci sequence:
    p = 1
    q = 1
    r = 0
    And de initial conditions 
    F0 = 0 
    F1 = 1

    # About the code

    lambda:
    Anonimus function, ideal to save time and memory
    in short methods
    
    Itertools:
    A python package that allow create iterators to 
    save memory and time

        accumulate
            Take two arguments
            first: a iterable (list, tuple, array)
            secord: a function 
            itertools.accumulate applies the function over pairs in
            the iterable

        repeat
            Make a iterator with the same argument 
            value n times
    """
    intermediate = itertools.accumulate(
        itertools.repeat(initial_values),
        lambda s, _: (s[1], p*s[1] + q*s[0] + r)
    )
    return map(lambda x: x[0], intermediate)

if __name__ == "__main__":
    # value entered by the user
    n = int(input('n: '))

    # Call the solution to recurrence function
    fibonacci = second_order(p=1, q=1, r=0, initial_values=(0, 1))
    
    print(list(next(fibonacci) for _ in range(n)))

