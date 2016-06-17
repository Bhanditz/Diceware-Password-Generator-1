#!/usr/bin/env python3
"""This python module generates n diceware passwords of length l, where l
denotes the number of words in the diceware password. The module uses a
cryptographically secure PRNG from the new python module 'secrets'. This
module assumes Python 3.6.
"""

import secrets


def generate(n, l):
    """This method prints n diceware passwords of length l.

    :param n: the number of generated diceware passwords
    :param l: the length of a diceware password
    :returns: prints to the console n diceware passwords of length l
    """
    for i in range(n):
        print("Password {0}:\t{1}".format(i + 1, password(l)))


def password(l):
    """This method returns a diceware password string of l words.

    This method samples cryptographically secure random integers using the
    new 'secrets' module from Python 3.6.

    :param l: the length of a diceware password
    :returns: str representing a diceware password of length l
    """

    passphrase = ""
    for i in range(l):
        passphrase += WORDLIST[secrets.randbelow(LENGTH)] + " "
    return passphrase


if __name__ == '__main__':
    n = int(input("How many Diceware passwords would you like? "))
    l = int(input("How many words should be in each Diceware password? "))
    print()

    WORDLIST = open('words.txt').read().split('\n')[:-1]
    LENGTH = len(WORDLIST)

    generate(n, l)
    print()
