def palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True



def palindrome(s):
    return s == s[::-1]
