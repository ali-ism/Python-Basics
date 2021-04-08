def ispalindrome(word):
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return ispalindrome(word[1:-1])

word = 'racexaecar'
b = ispalindrome(word)