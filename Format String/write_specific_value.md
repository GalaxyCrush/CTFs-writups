# Challenge `Write Specific Value` Writeup

- Vulnerability: Format String Vulnerability
- Where: On the printf function on the vuln() function
- Impact: It allows to the user to write in the arbitrary memory, namely on the target memory.

## Steps to reproduce

The logic is the same as in the previous challenge, but this time we want to write a specific value to the correct memory address and as previously determined, we control the seventh stack argument, and the "**\%7$n**" format specifier writes the number of characters printed so far to the memory address referenced by the seventh argument.

1. Since "**\%n**" writes the total number of printed characters, we need to ensure that 327 characters are printed before %7$n is executed. So we can implement a script that sends that payload.

2. The target memory address is sent as part of the input and occupies 4 bytes, which are already counted as printed characters. Therefore, we still need 323 additional characters to reach the desired total of 327. By adding padding using the %323x format specifier, we force printf to print the remaining 323 characters.

3. When "**\%7$n**" is evaluated, the value 327 is written to the target memory address, causing the verification to succeed and granting access to the flag: SSof{And_you_can_write_whatever_you_want}

[(POC)](POC/write_specific_value.py)
