# Challenge `Write Specific Byte` Writeup

- Vulnerability: Format String Vulnerability
- Where: On the printf function on the vuln() function
- Impact: It allows to the user to write in the arbitrary memory, namely on the target memory.

## Steps to reproduce

The logic is the same as in the previous challenges, but this time we want to write a specific byte to the correct memory address and as previously determined, we control the seventh stack argument, and the "**\%7$hhn**" format specifier writes the number of bytes written mod 258 printed so far to the memory address referenced by the seventh argument.

1. Since %hhn writes the number of bytes written mod 258, we need to ensure that the MSB of the target value is 0x02 to pass the verification.

2. The target memory address + 3(is the MSB of the address) is sent as part of the input and occupies 4 bytes, which are already counted as bytes to the "\%hnn". Therefore, we still need 254 additional bytes to reach the 0x02 result from the mod operation. By adding padding using the %254x format specifier, we are adding padding to the string and adding bytes.

3. After writting on the memory address of the target, the MSB will be 0x02.

[(POC)](POC/write_specific_byte.py)
