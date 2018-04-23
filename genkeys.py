### KEY GEN ###
import nacl
import nacl.public 


alice_private = nacl.public.PrivateKey.generate()                      #generate key object
#alice_public = nacl.public.PublicKey.generate()

privateHex = alice_private.encode(encoder=nacl.encoding.HexEncoder)    #encode PRIVATE KEY into hexedecimal, this makes it able to be written to a file
publicHex = alice_private.public_key.encode(encoder=nacl.encoding.HexEncoder)	#note that this is because the key is a number in memory, not a string...
									
fPriv = open("private.key", "w")                        #open new file private.key in "write mode"
fPriv.write(privateHex)                                 #write private key to file
fPriv.close()

fPub = open("public.key", "w")
fPub.write(publicHex)
fPub.close()															


