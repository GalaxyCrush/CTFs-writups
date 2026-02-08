# Challenge `Short Local Read` Writeup

- Vulnerability: Format String Vulnerability
- Where: On the printf function call in the vuln() function
- Impact: It allows to read arbitrary memory content and write to arbitrary memory addresses.

## Steps to reproduce

Its the same logic as the previous one, but now we have a smaller buffer, so we cant send the previous string. Its the same code, so when using gdb, using the same logic as the previous, we see that the register is the same as the previous, the seventh one, so we can send the following input to the server: "**%7$s**" that will print the content of the seventh register.

Doing this the output will be the flag: "SSof{Positional_arguments_ftw}"
