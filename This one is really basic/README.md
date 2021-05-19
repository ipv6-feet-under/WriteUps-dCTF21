This one is really basic
==================

As the title already says, this is really basic. And also it is just base64 encrypted 42 times.

[cipher.txt](cipher.txt)

So you can either put it in online tools like [CyberChef](https://gchq.github.io/CyberChef/), or you can use this [script:](thisoneisreallybasic.py)

```py
import base64

encodedStr = "PUT YOUR CIPHER HERE"

while True:
	decodedBytes = base64.b64decode(encodedStr)
	decodedStr = str(decodedBytes)

	if decodedStr[:4] == 'dctf':
		break
	else:
		encodedStr = decodedStr

print(decodedStr)

```

