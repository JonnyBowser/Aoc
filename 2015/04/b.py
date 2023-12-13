import hashlib

part = input()
for i in range(100000000):
    if hashlib.md5((part + str(i)).encode()).hexdigest()[:6] == "000000":
        print(i)
        break
