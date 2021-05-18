#!/usr/bin/python
# sp-box

import nclib
from string import ascii_letters, digits
from random import SystemRandom
from math import ceil, log

random = SystemRandom()
ALPHABET = ascii_letters + digits + "_!@#$%.'\"+:;<=}{"
newlist = list("")

nc = nclib.Netcat(('dctf1-chall-sp-box.westeurope.azurecontainer.io', 8888), verbose=False)
start = ">"

recv = nc.recv = nc.recv_until(start.encode('utf-8'))
a, flag, b = recv.splitlines()
flag = flag.decode('utf-8')

for character in ALPHABET:
	nc.send(character*2+'\n')
	recv = nc.recv_until(start.encode('utf-8'))
	a, newchar, b = recv.splitlines()
	newchar = newchar.decode('utf-8')
	newchar = newchar[1]
	newlist.append(newchar)


VORZWEI = {k : v for k, v in zip(ALPHABET, newlist)}


def decrypt(cipher):
	newcipher = ""
	for character in cipher:
		position = newlist.index(character)
		trans = ALPHABET[position]
		newcipher = newcipher + trans
	return newcipher

rounds = int(2*ceil(log(len(flag), 2)))

rounds = int(rounds/2)


for round in range(rounds):
	if round < (rounds):
		flag = decrypt(flag)
		print(str(round) + ' ' + flag)

nc.send(flag+'\n')
print(flag)

message = flag

while True:
	message =  [message[i] for i in range(len(message)) if i%2 == 1] + [message[i] for i in range(len(message)) if i%2 == 0]
	message = ''.join(message)
	if message[:4] == 'dctf':
		print(message)
		break

recv = nc.recv_all()
print(recv.decode('utf-8'))