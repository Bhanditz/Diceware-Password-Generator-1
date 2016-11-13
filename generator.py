#!/usr/bin/env python3
"""This program generates n Diceware passphrases of length k, where k
denotes the number of words in each passphrase. It uses a CSPRNG
from the 'secrets' module. It assumes Python 3.6+ is installed.
"""

from secrets import randbelow as nextInt


def generate(n, k):
    """Prints n Diceware passphrases of length k words each."""
    for i in range(n):
        print("Password {0}:\t{1}".format(i + 1, passphrase(k)))


def passphrase(k):
    """Returns a Diceware passphrase of length k words."""
    passphrase = ""
    for i in range(k):
        passphrase += word() + " "
    return passphrase.strip()


def word():
    """Returns a random word from the word list."""
    return wordlist[nextInt(numberOfWords)]


if __name__ == '__main__':
    wordlist = open('words.txt').read().split('\n')[:-1]
    numberOfWords = len(wordlist)
    
    n = int(input("How many Diceware passwords would you like? "))
    k = int(input("How many words should be in each password? "))
    
    print()
    generate(n, k)
    print()