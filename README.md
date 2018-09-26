
# Made by Ano.mobb


# Anogen 

offline-brainwallet-generator<br/>

#

```




Donate to the author of this program: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
```

#

# Installation

<b> Python 3.4.0 Required </b> 


Installation: 

```
$ git clone https://github.com/mobb111/anogen-master

$ cd anogen-master

$ pip install -r requirements.txt 
```

#

# Usage

$ cd anogen-master

$ python anogen.py
```
<br>

# Proof of Concept

This program create from passphrase privatekey, publickey,address and WIF, for more secure wallet u can use 
salt as a password.

Although this project can be used maliciously, it is simply an exploration into the Bitcoin protocol and advanced 
encryption and hashing techniques using Python.

#

# How it Works

From passphrase is generated privatekey, from private key publickey, from publickey address and final from privatekey 
WIF.

#

# Expected Outputs

# Sample printed:

Enter passphrases: abilities
Enter salt for sha256:
Passphrase:  abilities
Privatekey:  cfae417a8bcd2cfe163182bed6d7b730a0c57140cf27d4d0dd14fe2fc47b7c54
salt password:
Publickey:  04e2ed37bb576f9b9b438d928723f9cae14dfecbc83a26c4844a103e0ad6bb9a2ebba110abeb8a89699762e28560c4cfcc2e19df511b2f5eb865b270650f6eb318
Address:  14tGrPnSB7L6QSzxvSr5boVK7ULbdNgKNr
WIF:  b'5KPkWJ9BgBWWrGMzuqhuNXZpTUtNdEqvPsoo3WuWSmQeQwU3V9n'
cfae417a8bcd2cfe163182bed6d7b730a0c57140cf27d4d0dd14fe2fc47b7c54


In anogen-master.txt will save wallet info.

# Sample file anogen-master.txt:


Passphrases: abilities
address: 14tGrPnSB7L6QSzxvSr5boVK7ULbdNgKNr
private key: cfae417a8bcd2cfe163182bed6d7b730a0c57140cf27d4d0dd14fe2fc47b7c54
salt password: 
WIF private key: b'5KPkWJ9BgBWWrGMzuqhuNXZpTUtNdEqvPsoo3WuWSmQeQwU3V9n'
public key: 04e2ed37bb576f9b9b438d928723f9cae14dfecbc83a26c4844a103e0ad6bb9a2ebba110abeb8a89699762e28560c4cfcc2e19df511b2f5eb865b270650f6eb318
Donate to the author of this program: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn


# Sample wit salt password printed:

Enter passphrases: abilities
Enter salt for sha256: 123456
Passphrase:  abilities123456
Privatekey:  47c6dd73bf298f86a74ebafa3d3b686a7d2f28d0c8400a081e873f18a5fb9724
salt password: 123456
Publickey:  04ffbe1f5c970cbbfb142cd3e5eabbceede60257feb8e395354dd66032afced4245ad7a1134d098f1b4311153a954a40e30fa533eae1b3f75b55bce732f281a26c
Address:  1KbrweES1FHq6misNdmtKiqKqu16b6ZQum
WIF:  b'5JMu2LqSs1Q3TWCZTuRSJAzvc6y9z3L4dX2UuUQgB9h7t1Xp3Wi'
47c6dd73bf298f86a74ebafa3d3b686a7d2f28d0c8400a081e873f18a5fb9724

# Sample file anogen-master.txt:

Passphrases: abilities123456
address: 1KbrweES1FHq6misNdmtKiqKqu16b6ZQum
private key: 47c6dd73bf298f86a74ebafa3d3b686a7d2f28d0c8400a081e873f18a5fb9724
salt password: 123456
WIF private key: b'5JMu2LqSs1Q3TWCZTuRSJAzvc6y9z3L4dX2UuUQgB9h7t1Xp3Wi'
public key: 04ffbe1f5c970cbbfb142cd3e5eabbceede60257feb8e395354dd66032afced4245ad7a1134d098f1b4311153a954a40e30fa533eae1b3f75b55bce732f281a26c

With this program u can recover lost btc, so if u find program usefull please:


```
Donate to the author of this program: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
```

#
