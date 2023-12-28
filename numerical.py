#
# Find the sum of integers between start and end integers
# Eg. The sum of integers between 1 and 100 is 5050 
#

def sum_of_all_integers_v1(start: int, end: int) -> int:
    num_of_integers = (end - start) + 1
    return ((num_of_integers * (start + end)) // 2)

def sum_of_all_integers_v2(start: int, end: int) -> int:
    num_of_integers = (end - start) + 1
    return (num_of_integers * (num_of_integers + 1) // 2)

#
# Find out the given number is prime or not
#
def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num%i == 0:
                return False
        return True

#
# Pentegonal number
#
# Have the function PentagonalNumber(num) read num which will be a positive integer and 
# determine how many dots exist in a pentagonal shape around a center dot on the Nth iteration. 
# For example, in the image below you can see that on the first iteration there is only a single dot, 
# on the second iteration there are 6 dots, on the third there are 16 dots, and
# on the fourth there are 31 dots. 
#
# n=1    n=2       n=3
#                   *
#         $       * $ *
#  *    $ * $   * $ * $ * 
#        $ $     * $ $ *
#                 * * *
#

def pentegonal_number_v1(num: int) -> int:
    if num == 1:
        return 1
    return ((num - 1) * 5) + pentegonal_number_v1(num - 1)

import functools
def pentegonal_number_v2(num: int) -> int:
    # Prepare list [0, 5, 10, 15, 20....]
    pentegon_list = [((i-1)*5) for i in range(1, num+1)]
    # Add 1 to the result, because for n=1 it was 0 point in the list instead of 1.
    # So add 1 in reduce method
    return functools.reduce(lambda curr, prev: prev + curr, pentegon_list, 1)

#
# Factorial of a given number.
# Please note math.factorial is available already.
#
def factorial_v1(num: int) -> int:
    if num == 1 or num == 0:
        return 1
    return num * factorial_v1(num - 1)

def factorial_v2(num: int) -> int:
    result = 1 
    if num == 0 or num == 1:
        return 1
    for i in range(1, num+1):
        result *= i 
    return result

if __name__ == "__main__":
    print("************* sum_of_all_integers **************")
    print(sum_of_all_integers_v1(-3, 4))
    print(sum_of_all_integers_v1(1, 100))
    print(sum_of_all_integers_v1(1, 1000))
    print(sum_of_all_integers_v1(1, 10000))
    print(sum_of_all_integers_v2(1, 10000))
    print("************* is_prime **************")
    for i in range(0, 50):
        print(f"The number {i} is {'a prime number' if is_prime(i) else 'not a prime number'}")
    print("************* pentegonal_number **************")
    for i in range(1, 50):
        print(f"V1 => for {i} : {pentegonal_number_v1(i)}")
        print(f"V2 => for {i} : {pentegonal_number_v2(i)}")
    print("************* factorial number **************")
    print(factorial_v1(0))
    print(factorial_v2(0))
    print(factorial_v1(1))
    print(factorial_v2(1))
    print(factorial_v1(5))
    print(factorial_v2(5))
    print(factorial_v1(10))
    print(factorial_v2(10))
