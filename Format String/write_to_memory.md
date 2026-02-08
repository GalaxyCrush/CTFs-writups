# Challenge `Write to Memory` Writeup

- Vulnerability: Format String Vulnerability
- Where: On the printf function on the vuln() function
- Impact: It allows to the user to write in the arbitrary memory, namely on the target memory.

## Steps to reproduce

As stated in the problem description, after sending the string "AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x", we were able to observe that the seventh stack argument contains the value "41414141", which corresponds to "AAAA". This indicates that the seventh stack argument marks the beginning of the buffer variable, meaning we have control over it.

Since the target variable is global, it is not located on the stack but in the program’s data segment (.bss). By knowing its memory address, we can overwrite it using the "**\%7$n**" format specifier.

1. We can create a script that send as payload the program input with the the following format: "target_address + \%7$n" By placing the address of target as the seventh argument on the stack, "**\%7$n**" causes printf to write the number of characters printed so far to that address.

2. As a result, the value written is non-zero, causing the verification to succeed and the flag to be revealed, being: "SSof{You_can_write_wherever_you_want}"


[(POC)](POC/write_to_memory.py)
