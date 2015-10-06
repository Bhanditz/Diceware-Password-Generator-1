III. What is Diceware?
======================

Diceware
--------

**Diceware** is a method for creating passphrases, passwords, and other cryptographic variables using an ordinary die from a pair of dice as a hardware random number generator.

For each word in the passphrase, five rolls of the dice are required. The numbers from 1 to 6 that come up in the rolls are assembled as a five-digit number, e.g. *43146*. That number is then used to look up a word in a word list. In the English list *43146* corresponds to *munch*.

Entropy
-------

The bits of entropy for each word in our Diceware password can be calculated easily. The formula is of the form:

.. math::
   entropy \approx log_2 (\# \: of \: unique \: words)

Thus, for our particular word list of approximately 354986 unique words, the entropy per word is ~18.44 bits. A Diceware passphrase consisting of 6 words can have an an entropy as much as ~110.62 bits!

Recommended Use
---------------

Many people tend to use the same password for multiple online applications. Thus, whenever there's a breach of security in the application's database, the security of all your accounts using the same password is compromised. This is why I suggest you generate a couple of Diceware passwords (preferably for all your online accounts), each at least of length 6 words, even if you don't need them. After the passwords are generated, I recommend you use a password manager like LastPass or KeePass to store these passwords securely with a lengthy, but easy to remember master password.

My personal preference is to use a open source utility called GNU Privacy Guard (GPG) to encrypt a plaintext containing your Diceware passwords using your public key, and decrypt the Diceware passwords using your private key. Though the private key is stored on your computer, it is stored in an encrypted form using a (hopefully lengthy) passphrase you have supplied. The only caveat is that you must not lose your key-pair, where doing so means all your Diceware passwords are forever lost in encrypted form.
