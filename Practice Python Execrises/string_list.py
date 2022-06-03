# python execrises from www.practicepython.org

# Execrise 6

a_string = str(input("Please enter a word, that may be a palindrome: "))

# reverse the user input
"""
rev_string = a_string[::-1]

if a_string == rev_string:
    print(f"Your word {a_string} and {rev_string} are a palindrome.")
else:
    print(f"Your word {a_string} and {rev_string} are not a palindrome.")
"""

# using a functions
def reverse_word(word):
    s = ""

    for i in range(len(word)):
        s += word[len(word) - 1 - i]

    return s

def palindrome(word, rev_word):
    """Check if the given words are a palindrome"""
    if a_string == rev_word:
        return f"Your word {word} and {rev_word} are a palindrome."
    else:
        return f"Your word {word} and {rev_word} are not a palindrome."
    
if __name__=="__main__":
    r_string = reverse_word(a_string)
    print(palindrome(a_string, r_string))
