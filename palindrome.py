def palindrome(s):
    return s.lower() == s[::-1].lower()


print(palindrome("ASa"))
