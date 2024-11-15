import requests 

data={'a':'21bdc28f848422af0e8ff7e031a092e4',
   ...: 'b':'c9cdfba6 a3b809a0&a7e4ecec#6c804bf5'}

In [6]: res=requests.post("http://localhost:80",data)

In [7]: res.text
Out[7]: 'pwn.college{YA2SAzBcVgttdwggh6HdgNnvRpk.dFTOyMDL1kjMzQzW}\n'

