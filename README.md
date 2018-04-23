# senegalSend
### Send a public key encrypted file over ip and then decrypt it using private key. Requires pynacl cryptography library.

pynacl can be installed by running `pip install PyNaCl`

First off one should generate the keypair by running `python genKeys.py` this will create two files,
public.key and private.key. private.key *must* be in the folder with client.py and public.key *must* be in the folder
with host.py. The keys are created with the __Curve25519__ algorithim. 

Next the host should run host.py, if you want to bind to a specific ip change it in the file. Localhost is default.
The file must be specified in the first arguement, eg. `python host.py [file]`.

The client should run client.py, adjusting the ip in file if needed. The decrypted file will be displayed on
stdin (standard input).

#### LIMITATIONS:
Can only send a file of size 2048bytes or less. Ill fix this in probably the next few hours... :()

