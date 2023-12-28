#
# Utility methods
#

#
# "hello" => ["h","e","l","l","o"]
#
def strchtolist(str_: str) -> list:
    return [*str_]

#
# "how are you?" => ["how", "are", "you?"]
#
def strtolist(str_: str) -> list:
    return str_.split(" ")

#
# ["how", "are", "you?"] => "how are you?"
# ["h","e","l","l","o"]  => "hello"
#
def listtostr(list_: list) -> str:
    return ''.join(list_)

#
# "how are you?" => ["how", "are", "you"] 
#
def remove_splchars_tolist(str_: str) -> list:
    return [e for e in str_ if e.isalnum()]

#
# Puzzle 1 : Alphabet soup
# From the given string, arrange all the characters in ascending order
# Also, remove any special characters.
# Eg. "hello!! how are you?" should be "aeehhlloooruwy" 
#
def alphabet_soup(string: str) -> str:
    return listtostr(sorted(remove_splchars_tolist(string)))

#
# Puzzle 2 : Matching Characters
# 
# Have the function MatchingCharacters(str) take the str parameter being passed and 
# determine the largest number of unique characters that exists between a pair of matching 
# letters anywhere in the string. 
# For example: if str is "ahyjakh" then there are only two pairs of matching letters, 
# the two a's and the two h's. Between the pair of a's there are 3 unique characters: h, y, and j. 
# Between the h's there are 4 unique characters: y, j, a, and k. 
# So for this example your program should return 4. 
# Another example: if str is "ghececgkaem" then your program should return 5 
# because the most unique characters exists within the farthest pair of e characters. 
# The input string may not contain any character pairs, and in that case your program 
# should just return 0. 
# The input will only consist of lowercase alphabetic characters. 
# Examples Input: "mmmerme" Output: 3 Input: "abccdefghi" Output: 0
#
def matching_characters(str_: str) -> str:
    count = 0
    str_len = len(str_)
    for i in range(0,str_len):
        ch = str_[i]
        temp = 0
        for j in range(i+1,str_len):
            # Update the temp variable until next matching found
            if ch == str_[j]:
                break
            temp += 1
        ## Evaluation part
        # No matching string found until end of the string
        # So, reset the temp to zero to avoid altering the previous count
        if temp >= ((str_len-1)-i):
            temp = 0
        # Store the count to return
        if temp > count:
            count = temp
    return count

#
# Puzzle 3 : Palindrome
#
#
def is_palindrome(str_in: str) -> bool:
    str_in = str_in.replace(" ", "").lower()
    str_size = len(str_in) - 1
    for _str in str_in:
        if _str != str_in[str_size]:
            return False
            str_size -= 1
        else:
            return True
    return False

def is_palindrome_v2(string: str) -> bool:
    return (string.replace(" ", "").lower() == string[::-1].replace(" ", "").lower())

#
# Puzzle 4 : Longest word
#
# Find the longest word in the given sentence. Please don't consider punctuations.
# eg. "Hello!! How are you?" => "Hello"
#
def longest_word(string: str) -> str:
    words = [listtostr(remove_splchars_tolist(word))  for word in strtolist(string)]
    return max(words, key=len)

def longest_word_v2(string: str) -> str:
    words = list()
    for word in strtolist(string):
        new_word = ""
        for ch in word:
            if ch.isalnum():
                new_word += ch
        words.append(new_word)
    return max(words, key=len)

# 
# Puzzle 5 : Question mark string
#
# Find is there are numbers sum is 10 and there are 3 question marks between the 
# numbers in the strimg
#
# Have the function QuestionsMarks(str) take the str string parameter, which
# will contain single digit numbers, letters, and question marks, and check if
# there are exactly 3 question marks between every pair of two numbers that add
# up to 10. If so, then your program should return the string true, otherwise
# it should return the string false. If there aren't any two numbers that add
# up to 10 in the string, then your program should return false as well.
#
# For example: if str is "arrb6???4xxbl5???eee5" then your program should
# return true because there are exactly 3 question marks between 6 and 4, and 3
# question marks between 5 and 5 at the end of the string. 
#
def integer_value(char: str) -> (bool,int):
    result = True
    value = -1
    try:
        value = int(char)
    except ValueError as ex:
        result = False
    return (result, value)

def question_mark_str(string: str) -> bool:
    results = list()
    num_pairs = list()
    index = 0
    for pos, char in enumerate(string):
        result, value = integer_value(char)
        if result:
            num_pairs.append((pos, value))
    # If 3 numbers found in the string, return False
    if (len(num_pairs) % 2):
            return False
    for i in range(0, len(num_pairs), 2):
        start = num_pairs[i][0] + 1
        end = num_pairs[i+1][0]
        value1 = num_pairs[i][1]
        value2 = num_pairs[i+1][1]
        if ((value1 + value2) == 10) and (string[start:end].count('?') == 3):
            results.append(True)
    return any(results)

#
# Puzzle 6 : Letter Changes
#
# Take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet 
# (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string 
# (a, e, i, o, u) and finally return this modified string.
#
# Test case : "hello*3" => "Ifmmp*3"
#
def letter_changes(string: str) -> str:
    new_str = ""
    for ch in string:
        if ch.isalpha():
            next_ch = chr(ord(ch) + 1)
            if next_ch in "aeiou":
                next_ch = next_ch.upper()
            new_str += next_ch
        else:
            new_str += ch
    return new_str

#
# Puzzle 7 : Simple Sequence
#
# Have the function SimpleSymbols(str) take the str parameter being passed and determine 
# if it is an acceptable sequence by either returning the string true or false. 
# The str parameter will be composed of + and = symbols with several letters between them 
# (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. 
# So the string to the left would be false. 
# The string will not be empty and will have at least one letter. 
#
def simple_sequence(string: str) -> bool:
    # Adding dummy character before and after string to avoid index - 1 and index + 1 operations
    string = "=" + string + "="
    for i in range(len(string) - 1):
        if string[i].isalpha():
            if not string[i-1] == '+' or not string[i+1] == '+':
                return False
    return True

if __name__ == "__main__":
    test = "hello!! how are you?"
    ## Test utility methods
    print("****** Utility methods ******")
    print(_list:=strchtolist(test))
    print(listtostr(_list))
    print(remove_splchars_tolist(test))

    ## Test : Alphabet soup
    print("****** Alphabet soup ******")
    print(alphabet_soup(test))

    ## Test : Matching characters
    print("****** Matching characters ******")
    print(matching_characters("ahyjakh")) # => 4
    print(matching_characters("ghececgkaem")) # => 5
    print(matching_characters("mmmerme")) # => 2
    print(matching_characters("abccdefghi")) # => 0

    ## Test : Palindrome
    print("****** Palindrome ******")
    print(is_palindrome("Never odd or even")) # => True
    print(is_palindrome("are you sure")) # => False
    print(is_palindrome("eye")) # => True
    print(is_palindrome("racecar")) # => True
    print(is_palindrome("malayalam")) # => True
    print(is_palindrome("madam")) # => True

    print(is_palindrome_v2("Never odd or even")) # => True
    print(is_palindrome_v2("are you sure")) # => False

    ## Test : Longest word in the sentence
    print("****** Longest word ******")
    print(longest_word(test)) # "hello"
    print(longest_word_v2(test)) # "hello"

    # Test : Question mark string
    print("****** Question mark string ******")
    print(question_mark_str('aa6?9')) # => False
    print(question_mark_str('aa6??9')) # => False
    print(question_mark_str('aa6???9')) # => False
    print(question_mark_str('aa6???4')) # => True
    print(question_mark_str('aa6a???b4')) # => True
    print(question_mark_str('7?x?y?z3')) # => True
    print(question_mark_str('7?x?y?z3??5')) # => True
    print(question_mark_str('7?x?y?z3??5??5')) # => False
    print(question_mark_str('acc?7??sss?3rr1??????5')) # => True
    print(question_mark_str('arrb6???4xxbl5???eee5')) # => True

    # Test : Letter changes
    print("****** Letter changes ******")
    print(letter_changes("hello*3")) # => "Ifmmp*3"
    print(letter_changes("fun times!")) # => "gvO Ujnft!"

    # Test : Simple Sequence
    print("****** Letter changes ******")
    print(simple_sequence("++d+===+c++==a"))
