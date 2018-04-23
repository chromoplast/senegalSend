
### ABAP SERVER ###

import socket															#load the socket functions
import sys																#load the sys functions, we need this to grab arguements
import nacl
import nacl.public

fPub = open("public.key", "r")
Pub = fPub.read()														#we do this to make a var with type "string" from one with type "file"

serverPublic = nacl.public.PublicKey(Pub, encoder=nacl.encoding.HexEncoder)	#create a public key object
serverSealedBox = nacl.public.SealedBox(serverPublic)


sock = socket.socket()													#set up a new socket to use

port = 666																#name our port within the ip
sock.bind(("127.0.0.1",port))											#socket now uses our hostname and port

try:
	print("Welcome to ABAP SERVER:\nusing file: " + sys.argv[1])
except:
	sys.exit("ERROR: NO ARGUMENTS SPECIFIED, PLEASE TRY AGAIN\n")		#if no arg, exit

f = open(sys.argv[1], "r")												#open file from 1e argument in read-mode
serverFileToEncrypt = f.read()											#read file and store as variable

encryptedServerFile = serverSealedBox.encrypt(serverFileToEncrypt, encoder=nacl.encoding.HexEncoder)	#encrypt file using key, encode as hex
print(encryptedServerFile)
print("\nLENGTH OF STREAM: " + str(len(encryptedServerFile)))


sock.listen(5)															#listen for new connections, max backlog is 5.

while True:																#loop forever
	client, addr = sock.accept()										#sock.accept() gives 2 items as output. one is a new client object, and one is their address
	print("Reciving connection from:", addr)
	client.send(encryptedServerFile)
	client.close()														#Close client connection
	print("\n")
