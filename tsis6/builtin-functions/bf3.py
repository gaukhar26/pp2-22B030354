def is_palindrome(my_str):
    my_str = my_str.casefold()
    rev_str = reversed(my_str)

    if list(my_str) == list(rev_str):
        return True
    else:
        return False
