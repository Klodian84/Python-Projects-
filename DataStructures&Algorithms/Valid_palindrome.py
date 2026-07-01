""""
Valid Palindrome.
Given a string s,  determine if it is a palindrome.
Considering only alphanumeric characters
and ignoring cases , skip over, punctuation, spaces and special characters.
"""
def is_palindrome(s):
    l, r =0 , len(s)-1 # classic set up for this pattern.
    while l < r:
        while l < r and not s[l].isalnum(): # skip over not alphanumeric char. Move pointer +1
            l += 1
        while l < r and not s[r].isalnum() : # skip over not alphanumeric char. Move pointer -1
            r -= 1
        if s[l].lower() != s[r].lower(): # ignore case .
            return False # if not equal then we don't have a palindrome.
        l += 1 # move one step to the right
        r -= 1 # move one step to the right
    return True # The loop keeps running until the pointers meet in the middle.

if __name__ == "__main__":
    s = input("Please enter a string: ")
    res = is_palindrome(s)
    print("true" if res else "false")




