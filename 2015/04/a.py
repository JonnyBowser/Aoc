import hashlib

part = input()
for i in range(10000000):
    if hashlib.md5((part + str(i)).encode()).hexdigest()[:5] == "00000":
        print(i)
        break
