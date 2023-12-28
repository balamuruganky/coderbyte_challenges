import math

#
# Return the string true if any two numbers can be multiplied so that the answer is 
# greater than double the sum of all the elements in the array. 
# If not, return the string false.
#
def sum_double_vs_two_bigger_elem_multiplied(arr: list) -> bool:
    sorted_arr = sorted(arr, reverse=True)
    first_two_mult = sorted_arr[0] * sorted_arr[1]
    sum_double_arr = math.pow(sum(arr),2)
    if(sum_double_arr > first_two_mult):
        return True
    else:
        return False

#
# Have the function ScaleBalancing(strArr) read strArr which will contain two
# elements, the first being the two positive integer weights on a balance scale
# (left and right sides) and the second element being a list of available
# weights as positive integers. Your goal is to determine if you can balance
# the scale by using the least amount of weights from the list, but using at
# most only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"]
# then this means there is a balance scale with a weight of 5 on the left side
# and 9 on the right side. It is in fact possible to balance this scale by
# adding a 6 to the left side from the list of weights and adding a 2 to the
# right side. Both scales will now equal 11 and they are perfectly balanced.
# Your program should return a comma separated string of the weights that were
# used from the list in ascending order, so for this example your program
# should return the string 2,6
#
# There will only ever be one unique solution and the list of available weights
# will not be empty. It is also possible to add two weights to only one side of
# the scale to balance it. If it is not possible to balance the scale then your
# program should return the string not possible.
#

def is_balaceable(left: int, right: int, available1: int, available2: int) -> bool:
    return ((left + available1) == (right + available2) or
            (left + available2) == (right + available1) or
            (left + available1 + available2) == (right) or
            (left) == (right + available1 + available2))

def balance_weights(weighing_scale: list, available_weights: list) -> list:
    left = weighing_scale[0]
    right = weighing_scale[1]
    # Check is one weight can balance the weighing scale
    for weight in available_weights:
        if is_balaceable(left, right, weight, 0):
            return [weight]

    # Check two available weights can balance the weighing scale
    for i in range(0, len(available_weights)):
        for j in range(i+1, len(available_weights)):
            if is_balaceable(left, right, available_weights[i], available_weights[j]):
                return [available_weights[i], available_weights[j]]

    # If both the above cases are failed then return empty list
    return []

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

if __name__ == "__main__":
    print(sum_double_vs_two_bigger_elem_multiplied([31,32,33,34,35]))
    print("********** is_balaceable *************")
    print(balance_weights([0, 1],[1])) # => [1]
    print(balance_weights([0, 2],[2])) # => [2]
    print(balance_weights([3, 2],  [1])) # => [1]
    print(balance_weights([2, 5],  [1, 4])) # => [1,4]
    print(balance_weights([2, 5],  [9, 5, 1, 4])) # => [1,4]
    print(balance_weights([5, 9],  [1, 2, 6, 7])) # => [2,6]
    print(balance_weights([3, 4],  [1, 2, 7, 7])) # => [1]
    print(balance_weights([13, 4], [1, 2, 3, 6, 14])) # => [3,6]
    print(balance_weights([0, 1],  [3])) # => []
    print(balance_weights([1, 0],  [2, 4, 8])) # => []
