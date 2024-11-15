import requests

In [2]: res=requests.post("http://localhost:80",data={'a':'f6668df8c1304ce9ab9ab347f8d7e463'}
   ...: )

In [3]: res.text
Out[3]: 'pwn.college{U9KP84VqVuoC-4ZVihl1JdOnp4u.dhDOyMDL1kjMzQzW}\n'

