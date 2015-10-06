### Diceware-Password-Generator ###
This repository contains a module called generator.py, which generates Diceware passwords using a cryptographically secure random number generator.

#### Requirements ####
This module was written in python3 and on Ubuntu 15.04, so I recommend you run the module in that environment. The entropy generation is a combined effort from `/dev/random` and the package `haveged`. Thus, if you find a way to change those specific lines of code to work on another OS, it should work.

#### How to Use ####
 - Install the package `haveged`:
```
$ sudo apt-get install haveged
```

Inside `/etc/default/haveged`, make sure the following line is present:
`DAEMON_ARGS="-w 1024"`

And finally, to make sure `haveged` is configured to start on boot, run the following command in terminal:
```
$ update-rc.d haveged defaults
```
 - Download the repository and unzip.

 - Run the module. Here's an example shell session to illustrate this:
```
$ python3 generator.py
How many Diceware passwords would you like? 5
How many words should be in each Diceware password? 5

Password 1: calluna sinesaloum odontoblast leafier aunique 
Password 2: fortresses sycophancies beheader platos subsulphid 
Password 3: oude cune arborescent jutty santovena 
Password 4: tanist elida carbondale isthmian tomorrowness 
Password 5: mangelin cyniatria galvanotaxis liegemen fieberling

```

#### Recommendations ####
Many people tend to use the same password for multiple online applications. Thus, whenever there's a breach of security in the application's database, the security of all your accounts using the same password is compromised. This is why I suggest you generate a couple of Diceware passwords (preferably for all your online accounts), each at least of length 6 words, even if you don't need them. After the passwords are generated, I recommend you use a password manager like LastPass or KeePass to store these passwords securely with a lengthy, but easy to remember master password.

My personal preference is to use a open source utility called GNU Privacy Guard (GPG) to encrypt a plaintext containing your Diceware passwords using your public key, and decrypt the Diceware passwords using your private key. Though the private key is stored on your computer, it is stored in an encrypted form using a (hopefully lengthy) passphrase you have supplied. The only caveat is that you must not lose your key-pair, where doing so means all your Diceware passwords are forever lost in encrypted form.

#### NOTE ####
The method of generating the passphrases in this module does not strictly adhere to the method of Diceware. In Diceware password generation, 5 numbers ranging from 1 to 6 are randomly generated and concatenated. The resulting 5-digit number is a kind of 'key' in a key-value pair, where the 'value' is a word selected from a word list. Each word in a Diceware password is generated this way. In my implementation, I randomly generate a 5-digit number, which acts as a 'key', and select the corresponding 'value' or word. Each word in my solution is generated this way.

#### License ####
The project is licensed under the MIT license.
