# CS61A Discussion 1
# May 26 2024
# Kexin Wang

# Q1
# while and if
def race(x, y):
    # """The tortoise always walks x feet per minute, while the hare repeatedly
    # runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    # many minutes pass until the tortoise first catches up to the hare.
    #
    # >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    # 7
    # >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    # 10
    # """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes



# Q2
def fizzbuzz(n):
    assert n > 0
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                print('fizzbuzz')
            else:
                print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
    return n


# Q3
def is_prime(n):
    i = 1
    if n == 1:
        return False
    else:
        while i < n-1:
            if n % (i+1) == 0:
                return False
            else:
                i += 1
    return True


# Q4
# Return the number of unique digits in positive integer n.
def unique_digits(n):
    assert n > 0
    digit = str(n)
    count = 0
    for i in range(10):
        if str(i) in digit:
            count += 1
    return count


def has_digit(n,k):
    assert k >=0 and k < 10
    if n % k == 0:
        return True
    else:
        return False
