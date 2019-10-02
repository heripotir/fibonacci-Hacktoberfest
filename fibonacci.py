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
    """
    intermediate = itertools.accumulate(
        itertools.repeat(initial_values),
        lambda s, _: (s[1], p*s[1] + q*s[0] + r)
    )
    return map(lambda x: x[0], intermediate)

if __name__ == "__main__":
    n = int(input('n: '))
    fibonacci = second_order(p=1, q=1, r=0, initial_values=(0, 1))
    print(list(next(fibonacci) for _ in range(n)))

