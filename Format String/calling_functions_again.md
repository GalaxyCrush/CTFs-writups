# Challenge `Calling Functions Again` Writeup

- Vulnerability: Format String Vulnerability
- Where: On the printf function on the vuln() function
- Impact: It allows to the user to write in the arbitrary memory, namely override the function call after the print function.

## Steps to reproduce

The same logic used in the previous challenge can be applied here. By exploiting the format string vulnerability, it is possible to overwrite the Global Offset Table (GOT) entry of the puts function so that it points to the win function.

1. First, the address of the win function is obtained from the executable file. In this case, the address is 0x08049216.

2. Since the "**\%hhn**" format specifier writes only one byte (the number of characters printed so far mod 256), the target value must be written in parts. As the address is 4 bytes long, it is split and written byte by byte.

3. A script is used to build the payload by appending the addresses target, target + 1, target + 2, and target + 3, so that each byte of the value can be written to the correct memory location.

4. After placing the addresses in the payload, a character counter is tracked, taking into account the mod 256 behavior of "**\%hhn**". Padding is then calculated so that each "**\%hhn**" writes the correct byte value to its corresponding address.

5. Finally, after sending the crafted payload, the GOT entry of puts is overwritten with the address of win. When the program subsequently calls puts, execution is redirected to win, resulting in the flag being printed: SSof{you_GOT_me}.

Note:

- The %c format specifier is used to control the number of printed characters precisely. Unlike %x, which prints values read from the stack and may produce variable-length output, %c always prints a fixed number of characters. This makes the character counter deterministic and ensures that %hhn writes the intended byte values reliably.

[(POC)](POC/calling_functions_again.py)
