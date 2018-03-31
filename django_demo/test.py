import hashlib
import time

data = "123" + str(time.time()*1000).split(".")[0] + "6c355ed087b2324311a14340fd7d066a"
data = data.encode()
sign = hashlib.md5(data)
sign = sign.hexdigest()

print(sign)
print(str(time.time()*1000).split(".")[0])
