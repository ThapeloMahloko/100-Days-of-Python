'''
Assignment 1: Programming Basics

Module  :Engineering  Programming I
Code    :EPG125C

Student Name & Surname : Ntombikayise Paulah Makhubela
Student Number         : 223082574
'''

# Question 1
def donuts(count):
    """
    Given an integer count of the number of donuts, return a string in the format:
    'Number of donuts: <count>' where <count> is the number passed in.
    If the count is 10 or more, use the word 'many' instead of the actual count.

    Args:
        count (int): The number of donuts.

    Returns:
        str: A string indicating the number of donuts.
    
    Examples:
        donuts(5) -> 'Number of donuts: 5'
        donuts(23) -> 'Number of donuts: many'
    """
    #Write your code here:

    if count >=10:
        return "Number of donuts:many"
    else: 
        return "Number of donuts if many:"+ str(count)


# Question 2
def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last 2 characters of the original string.
    If the string length is less than 2, return an empty string.

    Args:
        s (str): The input string.

    Returns:
        str: A string composed of the first 2 and last 2 characters of s, or an empty string if s is too short.
    
    Examples:
        both_ends('spring') -> 'spng'
        both_ends('ab') -> 'abab'
        both_ends('a') -> ''
    """
    #Write your code here:

    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

# Question 3
def fix_start(s):
    """
    Given a string s, return a string where all occurrences of its first character 
    have been changed to *, except for the first character itself.

    Args:
        s (str): The input string.

    Returns:
        str: A string with all occurrences of the first character replaced by *, except the first one.
    
    Examples:
        fix_start('babble') -> 'ba**le'
        fix_start('aardvark') -> 'a*rdv*rk'
    """
    #Write your code here:

    if not s:
        return s
    else:
        return s[0] + s[1:].replace(s[0], '*')
# Question 4
def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b separated by a space,
    but with the first 2 characters of each string swapped.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Returns:
        str: A single string with the first 2 characters of a and b swapped, separated by a space.
    
    Examples:
        mix_up('mix', 'pod') -> 'pox mid'
        mix_up('dog', 'dinner') -> 'dig donner'
    """
    #Write your code here:
    swap_a= a[:2] + a[2:]
    swap_b = b[:2] + b[2:]
    return swap_b + ' ' + swap_a

# Question 5
def verbing(s):
    """
    Given a string s, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged.

    Args:
        s (str): The input string.

    Returns:
        str: The transformed string with 'ing' or 'ly' added, or unchanged if too short.
    
    Examples:
        verbing('hail') -> 'hailing'
        verbing('swimming') -> 'swimmingly'
        verbing('do') -> 'do'
    """
    #Write your code here:
    if  len(s) >= 3:
        if s[-3:] == 'ing':
            return s + 'ly'
        else:
            return s + 'ing'
    else:
        return s

# Question 6
def not_bad(s):
    """
    Given a string s, find the first appearance of the substring 'not' and 'bad'.
    If 'bad' follows 'not', replace the whole 'not'...'bad' substring with 'good'.
    Return the resulting string.

    Args:
        s (str): The input string.

    Returns:
        str: The string after replacing 'not'...'bad' with 'good'.
    
    Examples:
        not_bad('This movie is not so bad') -> 'This movie is good'
        not_bad('This dinner is not that bad!') -> 'This dinner is good!'
        not_bad('This tea is not hot') -> 'This tea is not hot'
    """
    #Write your code here:

    not_index = s.find('not')
    bad_index = s.find('bad')
    if  bad_index != -1 and not_index != -1 and bad_index > not_index:
        return s[:not_index] + 'good' + s[bad_index+3:]


def main():
    """
    Main function to test all the above functions to ensure they work as expected.
    """
    # Test donuts function
    print('Question 1')
    print(donuts(5))  # Expected: 'Number of donuts: 5'
    print(donuts(23))  # Expected: 'Number of donuts: many'

    # Test both_ends function
    print('Question 2')
    print(both_ends('spring'))  # Expected: 'spng'
    print(both_ends('ab'))  # Expected: 'abab'
    print(both_ends('a'))  # Expected: '' (empty string)

    # Test fix_sctart function
    print('Question 3')
    print(fix_start('babble'))  # Expected: 'ba**le'
    print(fix_start('aardvark'))  # Expected: 'a*rdv*rk'

    # Test mix_up function
    print('Question 4')
    print(mix_up('mix', 'pod'))  # Expected: 'pox mid'
    print(mix_up('dog', 'dinner'))  # Expected: 'dig donner'

    # Test verbing function
    print('Question 5')
    print(verbing('hail'))  # Expected: 'hailing'
    print(verbing('swimming'))  # Expected: 'swimmingly'
    print(verbing('do'))  # Expected: 'do'

    # Test not_bad function
    print('Question 6')
    print(not_bad('This movie is not so bad'))  # Expected: 'This movie is good'
    print(not_bad('This dinner is not that bad!'))  # Expected: 'This dinner is good!'
    print(not_bad('This tea is not hot'))  # Expected: 'This tea is not hot'


if _name_ == "_main_":
    main()




   