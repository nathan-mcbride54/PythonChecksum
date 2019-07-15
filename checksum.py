#!/usr/bin/env python3
import sys
import hashlib

BUFFER_SIZE = 128000  # lets read stuff in 128kb chunks!

Selected_hash = sys.argv[1]
if Selected_hash.lower() == "sha256":
	hash = hashlib.sha256()
elif Selected_hash.lower() == "sha1":
	hash = hashlib.sha1()
else:
	hash = hashlib.md5()

Expected_Hash = sys.argv[2]

# This defines the loop that reads the file through a buffer and  hashes it block by block
with open(sys.argv[3], 'rb') as f:
	while True:
		data = f.read(BUFFER_SIZE)
		if not data:
			break
		hash.update(data)

Hash_Result = str.format(hash.hexdigest())

# This compares the entered hash to the resultant hash
if Expected_Hash == Hash_Result:
	print("Hashes Match!")
else:
	print("Error: Hashes do not match!")

sys.stdout.flush()
