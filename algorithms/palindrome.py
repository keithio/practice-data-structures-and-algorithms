def is_palindrome(string):
    """
    Test if a provided string is a palindrome.
    """
    l = 0
    r = len(string) - 1

    for i in range(len(string)):
        # Skip non-alpha characters
        if not string[l].isalpha():
            l = l + 1
            continue

        if not string[r].isalpha():
            r = r - 1
            continue

        # Compare opposing positions of string
        if string[l].lower() != string[r].lower():
            return False

        # Shift indices
        l = l + 1
        r = r - 1

        # Terminate when at the center of the string
        if r - l <= 1:
            return True


if __name__ == '__main__':
    print is_palindrome('Able was I ere I saw Elba')
    print is_palindrome('A man, a plan, a canal - Panama!')
    print is_palindrome('Madam, I\'m Adam')
    print is_palindrome('My name is Keith.')
