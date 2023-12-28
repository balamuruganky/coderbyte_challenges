import math

def fib_infinity(start = 0, acc = 1):
    yield start + acc
    yield from fib_infinity(acc, start + acc)

def fib_recursive(num):
    if num <= 1:
        return num
    else:
        return fib_recursive(num - 1) + fib_recursive(num - 2)

def next_fibonacci(num):
    next_ = num * (1 + math.sqrt(5.0)) / 2.0
    return round(next_)

def prev_fibonacci(num):
    prev_ = num / ((1 + math.sqrt(5.0)) / 2.0)
    return round(prev_)

def fibonacci_index(num):
    _current  = 0
    _next     = 1
    _nextnext = 1

    if (num == 0):
        return 0
    elif (num == 1):
        return 1 # It can be either 1 or 2
    else:
        i = 2
        while _current < num:
            _current = _next + _nextnext
            _next = _nextnext
            _nextnext = _current
            i += 1
    return i if _current == num else -1

def is_fibonacci_v1(num):
    if (_index:=fibonacci_index(num)) != -1:
        print(f"It is {_index} position fibonacci number")
        return True
    else:
        return False

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return (num == (sqrt_num * sqrt_num))

def is_fibonacci_v2(num):
    return is_perfect_square(5.0*num*num + 4.) or is_perfect_square(5.0*num*num - 4.)

if __name__ == "__main__":
    i = fib_infinity()
    for _ in range(10):
        print(next(i))
    print("-----------------------------------------------")
    for i in range(10):
        print(fib_recursive(i))
    print("-----------------------------------------------")
    print(is_fibonacci_v1(9))
    print(is_fibonacci_v1(13))
    print(is_fibonacci_v1(144))
    print(is_fibonacci_v1(next_fibonacci(144)))
    print(is_fibonacci_v1(280571172992510140037611932413038677189525))
    print(is_fibonacci_v1(222232244629420445529739893461909967206666939096499764990979600))
    print("-----------------------------------------------")
    print(next_fibonacci(7778742049))
    print("-----------------------------------------------")
    print(prev_fibonacci(7778742049))
    print("-----------------------------------------------")
    print(is_fibonacci_v2(9))
    print(is_fibonacci_v2(13))
    print(is_fibonacci_v2(144))
    print(is_fibonacci_v2(next_fibonacci(144)))
    ## V2 is failing for bigger numbers... Really??? Need to debug
    #print(is_fibonacci_v2(280571172992510140037611932413038677189525))
    #print(is_fibonacci_v2(222232244629420445529739893461909967206666939096499764990979600))
    print("-----------------------------------------------")
