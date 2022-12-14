from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def RSADecrypt(encrypted_data,privatekeyfile):

 file_in = open(encrypted_data, "rb")
 private_key = RSA.import_key(open(privatekeyfile).read())
 enc_session_key, nonce, tag, ciphertext = \
 [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
 # Decrypt the session key with the private RSA key
 cipher_rsa = PKCS1_OAEP.new(private_key)
 session_key = cipher_rsa.decrypt(enc_session_key)

 # Decrypt the data with the AES session key
 cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
 data = cipher_aes.decrypt_and_verify(ciphertext, tag)
 f = open("decrypted_image.jpg","wb")
 f.write(data)
 f.close()
 return data
 
 #decrypt
RSADecrypt("image_encrypted_data.bin","private.pem")
 