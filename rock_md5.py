import hashlib

fo = open("rockyou.txt", "r")
line = fo.readline().strip()

fw = open("hash.txt", "w")

for line in fo:
   hash = hashlib.md5(line.strip().encode())
   fw.write(line.strip() + ":" + hash.hexdigest() + "\n")