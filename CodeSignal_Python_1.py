# Question: Implement a function that, given an integer n, uses a specific method on it
# and returns the number of bits in its binary representation.

# Answer: n is the input number
def solution(n):
    return n.bit_length()
#----------------------------------------------------------------------------------------------------------

# Question: Your task is to implement a function that, given a number n, returns -1 if this number is not
#  an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be
#  written without a decimal point.

# Answer: n is the input number
def solution(n):
    if type(n) == int:
        return n % 2
    else:
        return -1
#----------------------------------------------------------------------------------------------------------

# Question: Write a function that, given an array of integers arr, sorts its elements in ascending order.

# Answer: arr is the input array
def solution(arr):
    n = len(arr)
    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            j += 1
    return arr
#----------------------------------------------------------------------------------------------------------

# Question: Implement a function that, given an integer number n and a base x, converts n from base x
#  to base 16.

# Answer: n is the input integer and x is the base of n
def solution(n, x):
    return hex(int(n,x))[2:]
#----------------------------------------------------------------------------------------------------------

# Question:  create a simplified version of mex function. For the given set s and given an upperBound,
#  implement a function that will find its mex if it's smaller than upperBound or return upperBound instead.

# Answer:
def solution(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found
#----------------------------------------------------------------------------------------------------------

# Question: Let's call a list beautiful if its first element is equal to its last element, or if a list is empty.
#  Given a list a, your task is to chop off its first and its last element until it becomes beautiful.
#  Implement a function that will make the given a beautiful as described, and return the resulting list as an answer.

# Answer:
def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        first, *res, last = res
    return res
#----------------------------------------------------------------------------------------------------------

# Question: Implement a function that will change the very first symbol of the given message to uppercase,
#  and make all the other letters lowercase.

# Answer:
def solution(message):
    return message.capitalize()
#----------------------------------------------------------------------------------------------------------

# Question: Implement a function that will replace all multiple space characters in the given line of your
#  code with single ones. In addition, all leading and trailing whitespaces should be removed.

# Answer:
def solution(code):
    return ' '.join(code.split())
#----------------------------------------------------------------------------------------------------------

# Question: Implement a function that, given a piece of code and a positive integer x will turn each
#  tabulation character in code into x whitespace characters.

# Answer:
def solution(code, x):
    return code.replace('\t', ' '*x)
#----------------------------------------------------------------------------------------------------------

# Question: Implement a function that, given a feedback and the size of the screen, splits the feedback into lines so that:
# each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
# each line is at most size characters long;
# no line has trailing or leading spaces;
# each line should have the maximum possible length, assuming that all lines before it were also the longest possible.

# Answer:
import textwrap

def solution(feedback, size):
    return textwrap.wrap(feedback, size)
#----------------------------------------------------------------------------------------------------------

# Question: Given a word, check whether it is a palindrome or not.

# Answer:
def solution(word):
    return word == word[::-1]
#----------------------------------------------------------------------------------------------------------

# Question: Given the password you always use, your task is to encrypt it using the permutation cipher with the given key.
# Example
# For password = "iamthebest" and
# key = "zabcdefghijklmnopqrstuvwxy", the output should be
# solution(password, key) = "hzlsgdadrs"

# Answer:
def solution(password, key):
    table = str.maketrans(string.ascii_lowercase, key)
    return password.translate(table)
#----------------------------------------------------------------------------------------------------------

# Question: The track of time will be kept by a float number. It will be displayed on the board with the
#  set precision precision with center alignment, and it is guaranteed that it will fit in the screen.
#  Your task is to test the billboard. Given the time t, the width of the screen and the precision with
#  which the time should be displayed, return a string that should be shown on the billboard.
# Example: For t = 3.1415, width = 10, and precision = 2

# Answer:
def solution(t, width, precision):
    return "{0:.{1}f}".format(t,precision).center(width)
#----------------------------------------------------------------------------------------------------------

# Question: Implement a function that will turn the old-style string formating s into a new one so that the
#  following two strings have the same meaning:
# Example: s % (*args)
# s.format(*args)
# Example: For s = "We expect the %f%% growth this week", the output should be
# solution(s) = "We expect the {}% growth this week".

# Answer:
import re
def solution(s):
    return "%".join([re.sub("%([bcdeEfFgGnosxX])","{}",S) for S in s.split("%%")])
#----------------------------------------------------------------------------------------------------------

# Question: Given such commit, your task is go remove the username part from it and return the second part
#  as an answer.
# Example: For commit = "0??+0+!!someCommIdhsSt", the output should be
# solution(commit) = "someCommIdhsSt"

# Answer:
def solution(commit):
    return commit.translate({ord(i): None for i in '0?+!'})