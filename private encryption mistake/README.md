Private Encryption Mistake
==================

We are given this 
![image](images/blurred.png) 
which shows a rsa private key with parts of it covered.
Tbh we followed this WriteUp: https://blog.cryptohack.org/twitter-secrets (reps gehen raus an GucciGang und Klaus)

Translating the image to text we get:
```
-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEAupQ7hhy0AQR0LRMZgP/Kl6J3l2+U+wp1YyVB8oDYvslE3AXU
3igwX2LOYgG/JIHQ5UI2G/0Fu5iPPikh3JoUABGFyPwWsBLnohdBBtpvfRLprhbB
lsKwjZfLJIrRex+sSfkcT9zVs1VH4JfcJAbeBNK/aQdMqc1i4JQ1xsQny4ZH7TZe
CXBigK99+V05C+ENRS1uWi9ixgcbMWCCBHsTq0Kl5FIfPvVJVBr075bf7DdARSRU
Wx/FtKVMlWe/nGUTz/ezu2jOx69kd+hvtzX1JVkeY+AFi7Ldta2tNaH/8kitzoXK
JC+6A+LQXynmjQdH9RGsg7QygFjPvIcgwE8LHsMt62OKcIx5LMHlW4lvLK/EZMnr
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
ZEt6WwyEqHhPyP0CggEBAMplAvElBwRTMaT6FfWwi149Q+C1+ogaRc686CkCEs7p
zWjt4+Tg3cndxj/p2Q3Z1AzJH8h/vfZruAQHF/UFwXIAPmuzS1K0HgnNHxr355vs
AYfArpTJeyZoRttQOXvRhM+c887RWGXX278VVS5e5mh16Dn0rKpDcRnsVMahBhTg
+4XheX0zJRa3lOnoWgRLFGcJj9px4Gk7PkZnx24S2bCb7GUbisvtELkLfAvVcGIS
vvJGbeovAGpArRoaCbpnRL96N50zOWGqHeXJFljvNDvfpVAbykf+50d2VApvElQ3
/v7UHVZEfszMk3g1z+RLpgVmtltCsFvDSkDW9omfoJ0CggEBAIBfu08VPrN+B8iD
QpyO2BBUDei8fjdskpvehjWGDqzKNYDxdVcAdERtk6DSWuzpvwPNbTRm6u3v66yu
QkHn9gBlxX1sYe5P9ExqP2p+Au8hR/8s7bhVa8G53WX1Dl47QVSwbKVOWSWtQSwB
hiB9s1YqgAlhcKBWP6vFbavr3VBYY5ln/018rYvR1euDVTUVZdSMmbq3gScF4fhv
NESMd1Je7XjygbVTPJPi1PcT/SgyDRUwz0RPYIvLlA3qT9ae7s5WTp1fanv5MV6p
4LnekTQ/CVjWSorY7xdXTCMfBK1GF7WhVGG4fVSPX8QeIPKUxKkQXgKAFJrCSjj7
CLG5pPkCggEAflfmKUDTC4kfkXwoXzHxHkgialFPbszvzOmyB39q3E2pU5pFTChv
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              #  
#                                                              # 
#                                                              #  
-----END RSA PRIVATE KEY-----
```

The key is coded on 4096 bits like in the linked WriteUp. First we need to convert it to hexadecimal and find the patterns (028201) that mark the beginning of the parameters:


```
30820929020100*0282020100ba943b861cb40104742d131980ffca97a277976f94fb0a75632541f280d8bec944dc05d4de28305f
62ce6201bf2481d0e542361bfd05bb988f3e2921dc9a14001185c8fc16b012e7a2174106da6f7d12e9ae16c196c2b08d97cb248ad1
7b1fac49f91c4fdcd5b35547e097dc2406de04d2bf69074ca9cd62e09435c6c427cb8647ed365e09706280af7df95d390be10d452d
6e5a2f62c6071b316082047b13ab42a5e4521f3ef549541af4ef96dfec37404524545b1fc5b4a54c9567bf9c6513cff7b3bb68cec7
af6477e86fb735f525591e63e0058bb2ddb5adad35a1fff248adce85ca242fba03e2d05f29e68d0747f511ac83b4328058cfbc8720
c04f0b1ec32deb638a708c792cc1e55b896f2cafc464c9eb
```
```
644b7a5b0c84a8784fc8fd*0282010100*ca6502f12507045331a4fa15f5b08b5e3d43e0b5fa881a45cebce8290212cee9cd68ede3
e4e0ddc9ddc63fe9d90dd9d40cc91fc87fbdf66bb8040717f505c172003e6bb34b52b41e09cd1f1af7e79bec0187c0ae94c97b2668
46db50397bd184cf9cf3ced15865d7dbbf15552e5ee66875e839f4acaa437119ec54c6a10614e0fb85e1797d332516b794e9e85a04
4b1467098fda71e0693b3e4667c76e12d9b09bec651b8acbed10b90b7c0bd5706212bef2466dea2f006a40ad1a1a09ba6744bf7a37
9d333961aa1de5c91658ef343bdfa5501bca47fee74776540a6f125437fefed41d56447ecccc937835cfe44ba60566b65b42b05bc3
4a40d6f6899fa09d*0282010100*805fbb4f153eb37e07c883429c8ed810540de8bc7e376c929bde8635860eacca3580f175570074
446d93a0d25aece9bf03cd6d3466eaedefebacae4241e7f60065c57d6c61ee4ff44c6a3f6a7e02ef2147ff2cedb8556bc1b9dd65f5
0e5e3b4154b06ca54e5925ad412c0186207db3562a80096170a0563fabc56dabebdd5058639967ff4d7cad8bd1d5eb8355351565d4
8c99bab7812705e1f86f34448c77525eed78f281b5533c93e2d4f713fd28320d1530cf444f608bcb940dea4fd69eeece564e9d5f6a
7bf9315ea9e0b9de91343f0958d64a8ad8ef17574c231f04ad4617b5a15461b87d548f5fc41e20f294c4a9105e0280149ac24a38
fb08b1b9a4f9*02820100*7e57e62940d30b891f917c285f31f11e48226a514f6eccefcce9b2077f6adc4da9539a454c286f
```
Following the WriteUp we get:

p_lower_bits: 0x644b7a5b0c84a8784fc8fd

N_upper_bits: 0xba943b861cb40104742d131980ffca97a277976f94fb0a75632541f280d8bec944dc05d4de28305f
62ce6201bf2481d0e542361bfd05bb988f3e2921dc9a14001185c8fc16b012e7a2174106da6f7d12e9ae16c196c2b08d97cb248ad1
7b1fac49f91c4fdcd5b35547e097dc2406de04d2bf69074ca9cd62e09435c6c427cb8647ed365e09706280af7df95d390be10d452d
6e5a2f62c6071b316082047b13ab42a5e4521f3ef549541af4ef96dfec37404524545b1fc5b4a54c9567bf9c6513cff7b3bb68cec7
af6477e86fb735f525591e63e0058bb2ddb5adad35a1fff248adce85ca242fba03e2d05f29e68d0747f511ac83b4328058cfbc8720
c04f0b1ec32deb638a708c792cc1e55b896f2cafc464c9eb

q: 0xca6502f12507045331a4fa15f5b08b5e3d43e0b5fa881a45cebce8290212cee9cd68ede3
e4e0ddc9ddc63fe9d90dd9d40cc91fc87fbdf66bb8040717f505c172003e6bb34b52b41e09cd1f1af7e79bec0187c0ae94c97b2668
46db50397bd184cf9cf3ced15865d7dbbf15552e5ee66875e839f4acaa437119ec54c6a10614e0fb85e1797d332516b794e9e85a04
4b1467098fda71e0693b3e4667c76e12d9b09bec651b8acbed10b90b7c0bd5706212bef2466dea2f006a40ad1a1a09ba6744bf7a37
9d333961aa1de5c91658ef343bdfa5501bca47fee74776540a6f125437fefed41d56447ecccc937835cfe44ba60566b65b42b05bc3
4a40d6f6899fa09d

dp: 0x805fbb4f153eb37e07c883429c8ed810540de8bc7e376c929bde8635860eacca3580f175570074
446d93a0d25aece9bf03cd6d3466eaedefebacae4241e7f60065c57d6c61ee4ff44c6a3f6a7e02ef2147ff2cedb8556bc1b9dd65f5
0e5e3b4154b06ca54e5925ad412c0186207db3562a80096170a0563fabc56dabebdd5058639967ff4d7cad8bd1d5eb8355351565d4
8c99bab7812705e1f86f34448c77525eed78f281b5533c93e2d4f713fd28320d1530cf444f608bcb940dea4fd69eeece564e9d5f6a
7bf9315ea9e0b9de91343f0958d64a8ad8ef17574c231f04ad4617b5a15461b87d548f5fc41e20f294c4a9105e0280149ac24a38
fb08b1b9a4f9

dq_upper_bits: 0x7e57e62940d30b891f917c285f31f11e48226a514f6eccefcce9b2077f6adc4da9539a454c286f

We modify the get_p.py:
get_p.py
```py
from Crypto.Util.number import bytes_to_long, isPrime

e = 65537
q = 0xca6502f12507045331a4fa15f5b08b5e3d43e0b5fa881a45cebce8290212cee9cd68ede3e4e0ddc9ddc63fe9d90dd9d40cc91fc87fbdf66bb8040717f505c172003e6bb34b52b41e09cd1f1af7e79bec0187c0ae94c97b266846db50397bd184cf9cf3ced15865d7dbbf15552e5ee66875e839f4acaa437119ec54c6a10614e0fb85e1797d332516b794e9e85a044b1467098fda71e0693b3e4667c76e12d9b09bec651b8acbed10b90b7c0bd5706212bef2466dea2f006a40ad1a1a09ba6744bf7a379d333961aa1de5c91658ef343bdfa5501bca47fee74776540a6f125437fefed41d56447ecccc937835cfe44ba60566b65b42b05bc34a40d6f6899fa09d
dp = 0x805fbb4f153eb37e07c883429c8ed810540de8bc7e376c929bde8635860eacca3580f175570074446d93a0d25aece9bf03cd6d3466eaedefebacae4241e7f60065c57d6c61ee4ff44c6a3f6a7e02ef2147ff2cedb8556bc1b9dd65f50e5e3b4154b06ca54e5925ad412c0186207db3562a80096170a0563fabc56dabebdd5058639967ff4d7cad8bd1d5eb8355351565d48c99bab7812705e1f86f34448c77525eed78f281b5533c93e2d4f713fd28320d1530cf444f608bcb940dea4fd69eeece564e9d5f6a7bf9315ea9e0b9de91343f0958d64a8ad8ef17574c231f04ad4617b5a15461b87d548f5fc41e20f294c4a9105e0280149ac24a38fb08b1b9a4f9

for kp in range(3, e):
    p_mul = dp * e - 1
    if p_mul % kp == 0:
        p = (p_mul // kp) + 1
        if isPrime(p):
            print(f"Possible p: {p}")

```

and get the result:
```
$ python3 ./get_p.py 
Possible p: 29791686445775073485378700470209688335718177706599767642432504083590603114910076374929535053482398336851605342797663683613325223634063629847424638028935759548191149276444459783992147191929135013836982345753448569845230229718165110551230345888691646705997950698867501969060964411380209431748935915067011799337626156789024820682099339362534433158645112827474678232631566274100969788543100022629142380969830130845896177796223051219120025584473048998525682854193337862016303825590875971178405543808856045166697591214691035232105537035578197042255791258084056674958796585835075868860711296172300516953713039694526325704957
```

No we can try to reconstruct the RSA key:
PEM.py
```py
from Crypto.PublicKey import RSA

p =  29791686445775073485378700470209688335718177706599767642432504083590603114910076374929535053482398336851605342797663683613325223634063629847424638028935759548191149276444459783992147191929135013836982345753448569845230229718165110551230345888691646705997950698867501969060964411380209431748935915067011799337626156789024820682099339362534433158645112827474678232631566274100969788543100022629142380969830130845896177796223051219120025584473048998525682854193337862016303825590875971178405543808856045166697591214691035232105537035578197042255791258084056674958796585835075868860711296172300516953713039694526325704957
q = 0xca6502f12507045331a4fa15f5b08b5e3d43e0b5fa881a45cebce8290212cee9cd68ede3e4e0ddc9ddc63fe9d90dd9d40cc91fc87fbdf66bb8040717f505c172003e6bb34b52b41e09cd1f1af7e79bec0187c0ae94c97b266846db50397bd184cf9cf3ced15865d7dbbf15552e5ee66875e839f4acaa437119ec54c6a10614e0fb85e1797d332516b794e9e85a044b1467098fda71e0693b3e4667c76e12d9b09bec651b8acbed10b90b7c0bd5706212bef2466dea2f006a40ad1a1a09ba6744bf7a379d333961aa1de5c91658ef343bdfa5501bca47fee74776540a6f125437fefed41d56447ecccc937835cfe44ba60566b65b42b05bc34a40d6f6899fa09d
e = 65537
phi = (p-1)*(q-1)
d = pow(e,-1,phi)
N = q * p

key = RSA.construct((N,e,d,p,q))
pem = key.export_key('PEM')
print(pem.decode())
```

Using the script we get:

```
$ python3 ./PEM.py  
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```

Now we can login at ssh and use it to authenticate:

![image](images/flag.png)



