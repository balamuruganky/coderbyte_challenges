import math

#
# Find the enemy
#
# You must create a function that can read matrix of numbers stored in an array 
# which will be a 2D matrix that contains only the integers 1, 0, or 2. 
# Then from the position in the matrix where a 1 is, return the number of spaces 
# either left, right, down, or up you must move to reach an enemy which is represented by a 2.
#
# What are the Rules?
# You are able to wrap around one side of the matrix to the other. 
# For example if array is [“0000”, “1000”, “0002”, “0002”] then this is the board:
# 0 0 0 0
# 1 0 0 0
# 0 0 0 2
# 0 0 0 2
# For this board your program should return 2 because the closest enemy (2) is 
# 2 spaces away from the 1 by moving left to wrap to the other side and then moving down once. 
# The array will contain any number of 0’s and 2’s, but only a single 1. 
# It may not contain any 2’s at all as well, where in that case your program should return a 0.
#
# Test cases: Input: [“000”, “100”, “200”] | Output: 1
#             Input: [“0000”, “2010”, “0000”, “2002” ] | Output: 2

def calculate_distance(coord1, coord2):
    distance = math.fabs(coord2[0] - coord1[0]) + math.fabs(coord2[1] - coord1[1])
    return int(distance)

def find_enemy(arr):
    player = list()
    enemies  = list()
    # Convert ["0001", "0002"] to [[0 0 0 0], [0 0 0 2]]
    listoflists = [list(map(int, item)) for item in arr]

    # Fill in player and enemy location as list
    for row, lists in enumerate(listoflists):
        for col, elem in enumerate(lists):
            if(elem == 1):
                player.append([row, col])
            elif(elem == 2):
                enemies.append([row, col])

    results = []
    for enemy in enemies:
        results.append(calculate_distance(player[0], enemy))
    
    return min(results)

#
# Vowel square
#
# Have the function VowelSquare(strArr) take the strArr parameter being passed
# which will be a 2D matrix of some arbitrary size filled with letters from the
# alphabet, and determine if a 2x2 square composed entirely of vowels exists in
# the matrix. For example: strArr is ["abcd", "eikr", "oufj"] then this matrix
# looks like the following:
#
# a b c d
# e i k r
# o u f j
#
# Within this matrix there is a 2x2 square of vowels starting in the second row
# and first column, namely, ei, ou. If a 2x2 square of vowels is found your
# program should return the top-left position (row-column) of the square, so
# for this example your program should return 1-0. If no 2x2 square of vowels
# exists, then return the string "not found". If there are multiple squares of
# vowels, return the one that is at the most top-left position in the whole
# matrix. The input matrix will at least be of size 2x2.

def make_square(arr: list) -> list:
    square = list()
    for elem in arr:
        # From ["abcd", "eikr", "oufj"] => [[a b c d][e i k r][o u f j]]
        row = [*elem]
        square.append(row)
    return square

def check_all_vowels(arr: list) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if all(item in vowels for item in arr) else False

def vowel_square(arr: list) -> tuple:
    vowels = tuple()
    splited_squares = dict()
    square = make_square(arr)
    for i in range(0, len(square)-1):
        row = square[i]
        for j in range(0, len(row)-1):
            splited_squares[(i,j)] = [square[i][j], square[i][j+1],
                                      square[i+1][j], square[i+1][j+1]]
            if check_all_vowels(splited_squares[(i,j)]):
                vowels = (i,j)
                break
    return vowels

#
# Chessboard Travelling
#
# Have the function ChessboardTraveling(str) read str which will be a string 
# consisting of the location of a space on a standard 8x8 chess board with no pieces 
# on the board along with another space on the chess board. 
#
# The structure of str will be the following: 
# "(x y)(a b)" where (x y) represents the position you are currently on with 
# x and y ranging from 1 to 8 and (a b) represents some other space on the chess board 
# with a and b also ranging from 1 to 8 where a > x and b > y. 
#
# Your program should determine how many ways there are of traveling from (x y) on 
# the board to (a b) moving only up and to the right. 
# For example: if str is (1 1)(2 2) then your program should output 2 
# because there are only two possible ways to travel from space (1 1) on a chessboard 
# to space (2 2) while making only moves up and to the right. 
#

def number_of_paths(m, n):
    if(m == 1 or n == 1):
        return 1
    return number_of_paths(m-1, n) + number_of_paths(m, n-1)

def chessboard_travelling_v1(positions: list) -> int:
    return number_of_paths((positions[1][0] - positions[0][0])+1,
                           (positions[1][1] - positions[0][1])+1)

def chessboard_travelling_v2(positions: list) -> int:
    left_steps  = (positions[1][0] - positions[0][0])
    top_steps   = (positions[1][1] - positions[0][1])
    total_steps = left_steps + top_steps
    left_steps_permutations = math.factorial(left_steps)
    top_steps_permutations  = math.factorial(top_steps)
    total_steps_permutations  = math.factorial(total_steps)

    return (total_steps_permutations // (left_steps_permutations * top_steps_permutations))

if __name__ == "__main__":
    print("************** find_enemy ***************")
    print(find_enemy(["000", "100", "200"])) # => 1
    print(find_enemy(["0000", "2010", "0000", "2002"])) # => 2
    print(find_enemy(["2000", "0020", "0000", "0001"])) # => 3
    print(find_enemy(["0000", "1000", "0002", "0002"])) # => 4
    print(find_enemy(["1000", "0000", "0000", "0002"])) # => 6

    print("************** vowel_square ***************")
    print(vowel_square(["abcd", "eikr", "oufj"])) # => (1,0)
    print(vowel_square(['uu', 'ea'])) # => (0,0)
    print(vowel_square(['bu', 'ea'])) # => ()
    print(vowel_square(['uu', 'ez'])) # => ()
    print(vowel_square(['gg', 'ff'])) # => ()
    print(vowel_square(['aqrst', 'ukaei', 'ffooo'])) # => (1,2)
    print(vowel_square(['zmnboni', 'qxrqopz', 'bfoaaok', 'oxbduil'])) # => (2,4)

    print("************** chessboard_travelling ***************")
    print(chessboard_travelling_v1([(1,1),(2,2)])) # => 2
    print(chessboard_travelling_v1([(2,2),(4,3)])) # => 3
    print(chessboard_travelling_v1([(1,1),(4,2)])) # => 4
    print(chessboard_travelling_v1([(1,1),(3,3)])) # => 6
    print(chessboard_travelling_v1([(2,2),(3,3)])) # => 2
    print(chessboard_travelling_v1([(2,2),(4,3)])) # => 3
    print(chessboard_travelling_v1([(2,2),(8,3)])) # => 7
    print(chessboard_travelling_v1([(2,2),(3,4)])) # => 3
    print(chessboard_travelling_v1([(1,1),(4,4)])) # => 20
    print(chessboard_travelling_v1([(1,1),(8,8)])) # => 3432
    
    print(chessboard_travelling_v2([(1,1),(2,2)])) # => 2
    print(chessboard_travelling_v2([(2,2),(4,3)])) # => 3
    print(chessboard_travelling_v2([(1,1),(4,2)])) # => 4
    print(chessboard_travelling_v2([(1,1),(3,3)])) # => 6
    print(chessboard_travelling_v2([(2,2),(3,3)])) # => 2
    print(chessboard_travelling_v2([(2,2),(4,3)])) # => 3
    print(chessboard_travelling_v2([(2,2),(8,3)])) # => 7
    print(chessboard_travelling_v2([(2,2),(3,4)])) # => 3
    print(chessboard_travelling_v2([(1,1),(4,4)])) # => 20
    print(chessboard_travelling_v2([(1,1),(8,8)])) # => 3432
