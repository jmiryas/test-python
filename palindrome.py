def palindrome(s):
    # Ubah string menjadi lowercase dan balik string tersebut
    # Return true jika sama
    # Return false jika beda

    return s.lower() == s[::-1].lower()


print(palindrome("ASa"))
