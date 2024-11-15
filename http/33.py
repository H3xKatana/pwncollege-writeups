requests by default follow redirections

import requests

In [2]: res=requests.get('http://localhost')

In [3]: res.text
Out[3]: 'pwn.college{ky17MV5SwTbbuKRfpCcZkdJVtQs.dBDMzMDL1kjMzQzW}\n'

