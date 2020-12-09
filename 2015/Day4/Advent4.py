import re
import itertools
from hashlib import md5

key = "ckczppom"
num = 0
hash = md5((key + str(num)).encode())
while (not hash.hexdigest().startswith("0" * 5)):
	num += 1
	hash = md5((key + str(num)).encode())
print(num)

num = 0
hash = md5((key + str(num)).encode())
while (not hash.hexdigest().startswith("0" * 6)):
	num += 1
	hash = md5((key + str(num)).encode())
print(num)
