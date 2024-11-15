import requests

In [4]: data={
   ...:   "a": "0ac2ed83f67569101f1d41516837c2b6",
   ...:   "b": {
   ...:     "c": "d4453a56",
   ...:     "d": [
   ...:       "a20b718c",
   ...:       "430f6448 2b5bea76&72473bea#edf7df9a"
   ...:     ]
   ...:   }
   ...: }

In [5]: headers={'Content-Type':'application/json'}

In [6]: res=requests.post("http://localhost:80",headers=headers,json=data)

In [7]: res.text
Out[7]: 'pwn.college{IXy9l8y4E284cigIRA4Igq2hzpa.ddTOyMDL1kjMzQzW}\n
