from Crypto.PublicKey import RSA
# arguments are the name of private key and public key file name
def generateKeys(privatekeyfile,publickeyfile):
 key = RSA.generate(2048)
 private_key = key.export_key()
 file_out = open(privatekeyfile, "wb")
 file_out.write(private_key)
 file_out.close()
 public_key = key.publickey().export_key()
 file_out = open(publickeyfile, "wb")
 file_out.write(public_key)
 file_out.close()

generateKeys("private.pem","public.pem")