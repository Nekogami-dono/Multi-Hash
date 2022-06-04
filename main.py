#Multi Hash
import hashlib
#Hashing Algorithms
md5_hash = hashlib.md5()
sha1_hash = hashlib.sha1()
sha256_hash = hashlib.sha256()
sha512_hash = hashlib.sha512()

#ptf = input("Path to File: ")
f = open("test.png", "rb")
inputfile = f.read()
md5_hash.update(inputfile)
sha1_hash.update(inputfile)
md5_digest = md5_hash.hexdigest()
sha1_digest = sha1_hash.hexdigest()
print("md5: " + md5_digest)
print("sha1: " + sha1_digest)
