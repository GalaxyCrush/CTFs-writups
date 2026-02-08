from pwn import *
import re


SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25055

### run a remote process
s = remote(SERVER, PORT, timeout=9999)


data = s.recvuntil(b'FINISH)?\n')
print(data)

data_str = data.decode('utf-8')
target = int(re.search(r"until you get to (\d+)", data_str, re.IGNORECASE).group(1))
print(target)

current = int(re.search(r"CURRENT = (\d+)", data_str, re.IGNORECASE).group(1))
print(current)

while current != target:
    s.send(b"MORE\n")
    text = s.recvuntil(b'FINISH)?\n')
    print(text)
    
    text_str = text.decode('utf-8')
    current = int(re.search(r"CURRENT = (\d+)", text_str, re.IGNORECASE).group(1))
    print(current)


if current == target:
    s.send(b"FINISH\n")
    r = s.recv()
    print("\nFLAG:")
    print(r)

# É a mesma lógica dos requests, mas com as funções com os sockets