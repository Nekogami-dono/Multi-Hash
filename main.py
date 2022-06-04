#Multi Hash
from binascii import crc32
import hashlib, os, zlib, sys

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

#get file infos 
file_name = os.path.basename(ptf)
file_size = os.path.getsize(ptf)


#Create Log File
with open("hashlog.txt", "w") as log:
    log.write("File: " + file_name + "\n" + "Size: " + str(file_size) + " byte" + "\n" + "md5: " + md5_digest + "\n" + "sha1: " + sha1_digest + "\n" + "sha256: " + sha256_digest + "\n" + "sha512: " + sha512_digest)