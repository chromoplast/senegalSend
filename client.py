#### ABAP CLIENT ####

import socket                 #load functions for sockets
import nacl                   #load PyNaCl
import nacl.public


sock = socket.socket()                    #define a new socket
port = 666                                #define ip port to connect to

fPriv = open("private.key", "r")          #open private key
Priv = fPriv.read()

clientPrivate = nacl.public.PrivateKey(Priv, encoder=nacl.encoding.HexEncoder)#create a private key object using opend private key, key encoded as hexidecimal
clientSealedBox = nacl.public.SealedBox(clientPrivate)                        #create a sealed box using private key, for decryption of mesg

sock.connect(("127.0.0.1", port))	                                                    #127.0.0.1-> LOCALHOST
#while sock.recv(2048) != "":
encryptedServerFile = sock.recv(2048)	                                                #recev max amt of data as 2048bytes
print(clientSealedBox.decrypt(encryptedServerFile,encoder=nacl.encoding.HexEncoder))  #decode transmission using our private key(transmission encoded as hexidecimal)

sock.close                                                                            #shut it down

