#Multi Hash
import hashlib
#Hashing Algorithms
md5_hash = hashlib.md5()
sha1_hash = hashlib.sha1()
sha256_hash = hashlib.sha256()
sha512_hash = hashlib.sha512()

ptf = input("Path to File: ")

#read file
f = open(ptf, "rb")
inputfile = f.read()

md5_hash.update(inputfile)
sha1_hash.update(inputfile)
sha256_hash.update(inputfile)
sha512_hash.update(inputfile)

#hash to hex
md5_digest = md5_hash.hexdigest()
sha1_digest = sha1_hash.hexdigest()
sha256_digest = sha256_hash.hexdigest()
sha512_digest = sha512_hash.hexdigest()
#print hash
print("md5: " + md5_digest)
print("sha1: " + sha1_digest)
print("sha256: " + sha256_digest)
print("sha512: " + sha512_digest)
