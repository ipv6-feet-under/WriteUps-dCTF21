Just Take Your Time
====================

Looking at the [code](source/orig_just-take-your-time.py) this challange needs us to calculate a product first and then decrypting some DES.

Connecting with NC looks like:

![nc](images/nc.png)

We don't have much time because it answeres "You are not worthy" very fast so we need to set up a [script](source/just_take_your_time.py):

```py
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

### connecting to the socket and recieving until the '=':
nc = nclib.Netcat(('dctf-chall-just-take-your-time.westeurope.azurecontainer.io', 9999), verbose=True)
start = "="
recv = nc.recv_until(start.encode('utf-8'))
a, term  = recv.splitlines()

ding=ding.decode()

###Getting the factors from recv:
x = int(term.split(' ')[0])
y = int(term.split(' ')[2])

###Calculating and answering:
z=x*y
z = str(z)
nc.send(z + '\n')


###Recieving the next part - decryption
recv = nc.recv_exactly(180)
a, b, important, c  = recv.splitlines()
important = important.decode()
print('important: ' + important)
important = bytes.fromhex(important)

###decrypting the RES and sending back
decr = cipher.decrypt(important)
nc.send(decr + b'\n')


nc.recv_all()
```

The little script solved the calculation and the following DES and recieved the flag:

![flag](images/flag.png)

Setting up the WriteUp afterwards it looks like the script is failing sometimes. Didn't had time to debug.. maybe because of the length of the cipher or the time initialization... just restart when it's wrong.
