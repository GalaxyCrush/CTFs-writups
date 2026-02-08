# Challenge `Write Big Number` Writeup

- Vulnerability: Format String Vulnerability
- Where: On the printf function on the vuln() function
- Impact: It allows to the user to write in the arbitrary memory, namely on the target memory.

## Steps to reproduce

The logic is the same as in the previous challenges, but this time the goal is to write a 4‑byte value to the correct memory address. As previously determined, we control the 7th stack argument and the following ones, and the "**\%n$hhn**" format specifier writes one byte containing the number of characters printed so far mod 256 to the memory address referenced by the n‑th argument. In this challenge, we want to write 0xDEADBEEF to the target variable.

1. Since "**\%hhn**" writes only one byte (the printed character count modulo 256), the value must be written in sections. Because the value is 4 bytes long, it is split and written byte by byte.

2. A script is used to build the payload by appending the addresses target, target + 1, target + 2, and target + 3, so that each byte of the value can be written to the correct memory location.

3. After placing the addresses in the payload, a character counter is tracked, taking into account the %hhn modulo‑256 behavior. Padding is then calculated so that each "**\%hhn**" writes the correct byte value.

4. Finally, after sending the constructed payload, the target variable contains the desired value and the flag is printed: SSof{and_write_Very_BIIIIIG_numbers}

[(POC)](POC/write_big_numbers.py)
