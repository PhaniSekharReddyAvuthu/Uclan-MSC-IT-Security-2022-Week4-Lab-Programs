from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def RSAEncrypt(data,publickeyfile,encryptedfile):
 
 file_out = open(encryptedfile, "wb")
 recipient_key = RSA.import_key(open(publickeyfile).read())
 session_key = get_random_bytes(16)
 # Encrypt the session key with the public RSA key
 cipher_rsa = PKCS1_OAEP.new(recipient_key)
 enc_session_key = cipher_rsa.encrypt(session_key)
 # Encrypt the data with the AES session key
 cipher_aes = AES.new(session_key, AES.MODE_EAX)
 ciphertext, tag = cipher_aes.encrypt_and_digest(data)
 [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag,ciphertext) ]
 file_out.close()


#encrypt
data = "This is the message I want to transmit after encrypting with rsa".encode("utf-8")
RSAEncrypt(data,"public.pem","encrypted_data.bin")