#Multi Hash
from tqdm import tqdm  
import hashlib, os, zlib

#Hashing Algorithms
md5_hash = hashlib.md5()
sha1_hash = hashlib.sha1()
sha256_hash = hashlib.sha256()
sha512_hash = hashlib.sha512()
sha3512_hash = hashlib.sha3_512()


#Get File Input
ptf = input("Path to File: ")


#get file infos 
file_name = os.path.basename(ptf)
file_size = os.path.getsize(ptf)

with tqdm(total=file_size, unit='B', unit_scale=True, miniters=1, desc=os.path.basename(ptf), leave=False) as t:
    chunk_size = 65536
    crcval = 0
    with open(ptf, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
                crcval = zlib.crc32(chunk, crcval)
                md5_hash.update(chunk)
                sha1_hash.update(chunk)
                sha256_hash.update(chunk)
                sha512_hash.update(chunk)
                sha3512_hash.update(chunk)
                t.update(len(chunk))
        t.update(abs(file_size-t.n))
        t.close()

#hash to hex
crc32_hash = (f'{crcval & 0xFFFFFFFF:08x}')
md5_digest = md5_hash.hexdigest()
sha1_digest = sha1_hash.hexdigest()
sha256_digest = sha256_hash.hexdigest()
sha512_digest = sha512_hash.hexdigest()
sha3512_digest = sha3512_hash.hexdigest()

#print hash
print("crc32: " + crc32_hash)
print("md5: " + md5_digest)
print("sha1: " + sha1_digest)
print("sha256: " + sha256_digest)
print("sha512: " + sha512_digest)
print("sha3_512: " + sha3512_digest)


#Create Log File
with open("hashlog.txt", "w") as log:
    log.write("File: " + file_name + "\n" + "Size: " + str(file_size) + " byte" + "\n" + "CRC32: " + crc32_hash + "\n" + "md5: " + md5_digest + "\n" + "sha1: " + sha1_digest + "\n" + "sha256: " + sha256_digest + "\n" + "sha512: " + sha512_digest + "\n" + "sha3_512: " + sha3512_digest)
