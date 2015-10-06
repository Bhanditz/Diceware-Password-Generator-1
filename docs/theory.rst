III. What is Diceware?
======================

Diceware
--------

**Diceware** is a method for creating passphrases, passwords, and other cryptographic variables using an ordinary die from a pair of dice as a hardware random number generator.

For each word in the passphrase, five rolls of the dice are required. The numbers from 1 to 6 that come up in the rolls are assembled as a five-digit number, e.g. *43146*. That number is then used to look up a word in a word list. In the English list *43146* corresponds to *munch*.

Entropy
-------

The bits of entropy for each word in our Diceware password can be calculated easily. The formula is of the form $log_2 (\# of unique words)$.

Thus, for our particular word list of approximately 354986 unique words, the entropy per word is ~18.44 bits. A Diceware passphrase consisting of 6 words can have an an entropy as much as 110.62 bits.
