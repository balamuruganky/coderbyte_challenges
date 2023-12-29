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

def find_enemy(arr: list) -> int: 
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

#
# Maximum Area
#
# Have the function MaximalSquare(strArr) take the strArr parameter being passed which will be a 
# 2D matrix of 0 and 1's, and determine the area of the largest square submatrix that contains all 1's.
# A square submatrix is one of equal width and height, and your program should return the area of the 
# largest submatrix that contains only 1's. 
# For example: if strArr is ["10100", "10111", "11111", "10010"] then this looks like the following matrix: 
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0 
#
# For the input above, you can see the bolded 1's create the largest square submatrix of size 2x2, 
# so your program should return the area which is 4. You can assume the input will not be empty. 
#
# Hard challenges are worth 15 points and you are not timed for them.
# 
# Sample Test Cases
#
# Input:["0111", "1111", "1111", "1111"]
#
# Output:9
#
# Input:["0111", "1101", "0111"]
#
# Output:1
#

def is_valid_area(square_input: list, x: int, y: int, dim: int) -> bool:
    area = 1;
    for i in range(x, dim+x):
        for j in range(y, dim+y):
            area *= square_input[i][j]
    return (True, dim*dim) if area == 1 else (False, 0)

def maximum_area(arr: list) -> int:
    square_input = [list(map(int, item)) for item in arr]
    row_length = len(square_input)
    col_length = len(square_input[0])
    filter_length = min(row_length, col_length)

    for square_dim in range(filter_length, 0, -1):
        for row in range(0, len(square_input) - square_dim+1):
            for col in range(0, len(square_input[row]) - square_dim+1):
                ret, area = is_valid_area(square_input, row, col, square_dim)
                if ret == True:
                    return area 
    return 0

#
#
# Have the function EightQueens(strArr) read strArr which will be an array
# consisting of the locations of eight Queens on a standard 8x8 chess board
# with no other pieces on the board. The structure of strArr will be the
# following: ["(x,y)", "(x,y)", ...] where (x,y) represents the position of the
# current queen on the chessboard (x and y will both range from 1 to 8 where
# 1,1 is the bottom-left of the chessboard and 8,8 is the top-right). Your
# program should determine if all of the queens are placed in such a way where
# none of them are attacking each other. If this is true for the given input,
# return the string "true" otherwise return the first queen in the list that is
# attacking another piece in the same format it was provided.
# 
# For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)",
# "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true.
# The corresponding chessboard of queens for this input is below (taken from
# Wikipedia). 
#

def is_valid_pos(queen1_pos: list, queen2_pos: list) -> bool:
    return ((queen1_pos != queen2_pos) and 
            (queen1_pos[0] == queen2_pos[0] or
             queen1_pos[1] == queen2_pos[1] or
            (queen1_pos[0] + queen1_pos[1]) == (queen2_pos[0] + queen2_pos[1]) or
            (queen1_pos[0] - queen1_pos[1]) == (queen2_pos[0] - queen2_pos[1])))

def eight_queens(arr: str):
    queen_postions = list()
    for coords in arr:
        num = None
        pairs = list()
        for ch in coords:
            if ch.isdecimal():
                if num is None:
                    num = int(ch)
                    pairs.insert(0, num)
                else:
                    num = int(ch)
                    pairs.insert(1, num)
        queen_postions.append(pairs)

    for queen1 in range(len(queen_postions)-1):
        for queen2 in range(queen1+1, len(queen_postions)):
            if is_valid_pos(queen_postions[queen1], queen_postions[queen2]):
                return queen_postions[queen1]

    return True

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

    print("************** maximum_area ***************")
    print(maximum_area(["0111", "1111", "1111", "1111"])) # => 9
    print(maximum_area(["10100", "10111", "11111", "10010"])) # => 4
    print(maximum_area(["10111", "10111", "11111", "11010"])) # => 9
    print(maximum_area(["011", "111","000"])) # => 4

    print("************** eight_queens ***************")
    print(eight_queens(['(2,1)', '(4,2)', '(6,3)', '(8,4)', '(3,5)', '(1,6)', '(7,7)', '(5,8)'])) # => True
    print(eight_queens(['(2,1)', '(4,2)', '(6,3)', '(8,4)', '(5,5)', '(3,6)', '(1,7)', '(7,8)'])) # => [6,3]
    print(eight_queens(['(2,1)', '(4,2)', '(4,4)', '(8,4)', '(3,4)', '(1,6)', '(7,7)', '(5,8)'])) # => [4,2]
    print(eight_queens(['(2,1)', '(4,2)', '(6,3)', '(8,3)', '(3,4)', '(1,6)', '(7,7)', '(5,8)'])) # => [6,3]
    print(eight_queens(['(2,1)', '(4,3)', '(6,3)', '(8,4)', '(3,4)', '(1,6)', '(7,7)', '(5,8)'])) # => [2,1]
    print(eight_queens(['(2,1)', '(4,2)', '(3,3)', '(8,4)', '(7,5)', '(3,6)', '(1,7)', '(7,8)'])) # => [4,2]
    print(eight_queens(['(2,1)', '(5,3)', '(6,3)', '(8,4)', '(3,4)', '(1,8)', '(7,7)', '(5,8)'])) # => [5,3]
