#!/usr/bin/env python3
"""This python module generates n diceware passwords of length l, where l 
denotes the number of words in the diceware password.  This module assumes that 
the 'haveged' package is installed on your linux system, as it provides 
excellent entropy.
"""

from os import system


def generate(n, l):
    """This method prints n diceware passwords of length l.
    
    The method references the password() method for generation of diceware 
    passwords.
    
    :param n: the number of generated diceware passwords
    :type n: int
    :param l: the length of a diceware password
    :type l: int
    :returns: prints to the console n diceware passwords of length l 
    """
    for i in range(n):
        print("Password {0}:\t{1}".format(i + 1, password(l))) 

def password(l):
    """This method prints a diceware password of length l.
    
    This method samples cryptographically secure random integers using the 
    linux coreutils shuf package.  One of the requirements for this module is 
    that the haveged package is installed as it allows /dev/random's entropy 
    pool to never dip below ~1024 bits.

    :param l: the length of a diceware password
    :type l: int
    :returns: str representing a diceware password of length l
    """
    # The {0} is substituted with the number of words in the wordlist (but -1 
    # because we start counting from 0).  And the {1} is substituted with l, or 
    # the number of words needed in the diceware password.
    system('shuf --input-range=0-{0} --random-source=/dev/random \
            --head-count={1} --output=numbers.txt'.format(LENGTH - 1, l))

    # Simply converting the randomly sampled integers from string from to int.
    numbers = [int(i) for i in open('numbers.txt').read().split('\n')[:-1]]
    system('rm numbers.txt')

    passStr = ''
    for number in numbers:
        passStr += WORDLIST[number] + ' '
    return passStr


if __name__ == '__main__':
    n = int(input("How many Diceware passwords would you like? "))
    l = int(input("How many words should be in each Diceware password? "))
    print()

    WORDLIST = open('words.txt').read().split('\n')[:-1]
    LENGTH = len(WORDLIST)

    generate(n, l)
    print()
