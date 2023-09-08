import hashlib

string = input('Digite a string: ')

# hash SHA-1
hash = hashlib.sha1()
hash.update(string.encode('utf-8'))

# Calcule o hash SHA-1
resp = hash.hexdigest()

print(resp)
