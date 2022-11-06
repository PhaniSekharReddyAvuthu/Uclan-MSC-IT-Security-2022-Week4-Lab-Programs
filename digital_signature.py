from Crypto.PublicKey import RSA

keyPair = RSA.generate(bits=1024)

# RSA sign the message
msg = b'A message for signing'
from hashlib import sha512
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d;, keyPair.n)


# RSA verify signature
msg = b'A message for signingg'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)


# RSA verify signature (tampered msg)
#msg = b'A message for signing (tampered)'
#hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
#hashFromSignature = pow(signature, keyPair.e, keyPair.n)
#print("Signature valid (tampered):", hash == hashFromSignature)