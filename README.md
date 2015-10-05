### Diceware-Password-Generator ###
This repository contains a module, generator.py, which generates Diceware passwords using a cryptographically secure random number generator.

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
