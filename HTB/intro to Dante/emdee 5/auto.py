import requests
import hashlib
import re

url="http://157.245.37.27:30594/"

r=requests.session()
out=r.get(url)
out=re.search("<h3 align='center'>+.*?</h3>",out.text)
out=re.search("'>.*<",out[0])
out=re.search("[^|'|>|<]...................",out[0])

out=hashlib.md5(out[0].encode('utf-8')).hexdigest()

print("sending md5 :-{}".format(out))

data={'hash': out}
out = r.post(url = url, data = data)

print(out.text)


>HTB{N1c3_ScrIpt1nG_B0i!}</p><center><form action="" method="post">