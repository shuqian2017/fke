import hashlib

m = hashlib.md5()
m.update('hello world!')
print(m.hexdigest())

