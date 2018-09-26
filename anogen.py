#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Ano.Mobb
# Rubygen/Ruby generator
# Donate: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
# -*- coding: utf-8 -*-
import os, binascii, ecdsa, urllib, json, codecs, time, queue
import hashlib, base58, sys, random, string, requests, base64, operator

class pause:
    p = 0


print ("""


           ____________________________________________________
           |                                                  |
           |   ___________________________________________    |
           |   |                                         |    |
           |   |  C:\>_offline-brainwallet-generator     |    |
           |   |  C:\>_(1)Enter passphrases u want to    |    |
           |   |       generate:                         |    |
           |   |                                         |    |
           |   |  C:\>_ (2)Enter pass for salt:          |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |   C:\>_Author: Ano.Mobb                 |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
                              -Ano.Mobb-
             Donate: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn

""")













a = input("Enter passphrases: ")
e = input("Enter salt for sha256: ")
v = (str(a))+(e)
privatekey = hashlib.sha256(v.encode("utf-8")).hexdigest()
key = binascii.unhexlify(privatekey)
s = ecdsa.SigningKey.from_string(key, curve = ecdsa.SECP256k1)
publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
c = '0'; byte = '00'; zero = 0
var = hashlib.new('ripemd160')
var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
a = (byte + var.hexdigest())
doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
address = a + doublehash[0:8]
for char in address:
    if (char != c):
        break
    zero += 1
zero = zero // 2
n = int(address, 16)
output = []
while (n > 0):
    n, remainder = divmod (n, 58)
    output.append(alphabet[remainder])
count = 0
while (count < zero):
    output.append(alphabet[0])
    count += 1
address = ''.join(output[::-1])
var80 = "80"+(privatekey) 
var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
WIF = str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))))
file = open("brainwallet-anogen.txt","a")
file.write("Passphrases: " + str(v) + "\n" +
           "address: " + str(address) + "\n" +
           "private key: " + (privatekey) + "\n" +
           "salt password: " +(e) +"\n" +
           "WIF private key: " + (WIF) + "\n" +
           "public key: " + (publickey) + "\n" +
           "Donate to the author of this program: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn" + "\n" + "\n")


file.close()

print ("Passphrase: " + ' ' + str(v))
print ("Privatekey: " + ' ' + str(privatekey))
print ("salt password: " +(e))
print ("Publickey: " + ' ' + str(publickey))
print ("Address: " + ' ' + str(address))
print ("WIF: " + ' ' + str(WIF))

























print (privatekey)
