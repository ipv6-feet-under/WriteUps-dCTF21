#!/usr/bin/python
# Just take your time DCTF

import itertools
import nclib
import sys
import collections
from Crypto.Cipher import DES3
from time import time


key = str(int(time())).zfill(16).encode("utf-8")

cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")



nc = nclib.Netcat(('dctf-chall-just-take-your-time.westeurope.azurecontainer.io', 9999), verbose=True)
start = "="
recv = nc.recv_until(start.encode('utf-8'))
print("\n" + recv.decode())

a, ding  = recv.splitlines()

ding=ding.decode()
print(ding)

x = int(ding.split(' ')[0])
y = int(ding.split(' ')[2])



z=x*y
z = str(z)

print(z)

nc.send(z + '\n')



recv = nc.recv_exactly(180)
a, b, wichtig, c  = recv.splitlines()

wichtig = wichtig.decode()
print('wichtig: ' + wichtig)
wichtig = bytes.fromhex(wichtig)


coolio = cipher.decrypt(wichtig)

nc.send(coolio + b'\n')


nc.recv_all()