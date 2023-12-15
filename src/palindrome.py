# function which return reverse of a string
# example: 
# katak -> true == "katak"
# bobo -> false != "obob"
def is_palindrome(s):
    return s == s[::-1]