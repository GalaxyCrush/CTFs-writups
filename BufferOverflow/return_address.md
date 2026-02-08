# Challenge `Return Address` writeup

- Vulnerability: Buffer Overflow
- Where: In the buffer on the challenge function, and the use of gets.
- Impact: Allows to change the information on another memory locations, in this case on the return value of the function. (eip registry).

## Steps to reproduce

1. Analyze the source code, and note that the buffer has a limit of 10 characters.
2. To alter the return value, we need to overflow the buffer. To do that we can implement a script that sends a string greater than 10 chars to alter the return address.
3. Executing the program with gdb, we can set a breakpoint at `challenge` function and save the memory location of the buffer, in this case `0xffffc076`, and the memory location of the EIP register that was `0xffffc08c`.
4. With both memory addresses, we can calculate the offset necessary for the buffer overflow to reach the return value (doing EIP address minus buffer address) which is `0x16` (22 bytes in decimal).
5. Now we need to find the memory address of the `win` function, which is `0x080486f1` (also gathered by using gdb).
6. Build the payload: 22 bytes of padding + address of `win()` in little-endian format (`\xf1\x86\x04\x08`).
7. Executing the script gives us the flag: `SSof{Buffer_Overflow_to_control_local_variables}`

[(POC)](POC/return.py)