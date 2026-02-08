# Challenge `Simple Local Read` Writeup

- Vulnerability: Format String Vulnerability
- Where: On the printf function call in the vuln() function
- Impact: It allows to read arbitrary memory content and write to arbitrary memory addresses.

## Steps to reproduce

The given code show us that the vuln() function uses a printf() with the raw user input, where the buffer that is printted has the necessary lenght to exploit at most 10 registers.
Using the GDB we can know the register that the variable of the flag (**secret_value**) is in.

1. In the gdb we can put a breakpoint on the printf fucntion call and then see the local variables that are alocated and where, giving so the memory address.

2. The register is the seventh one, so we can send as user input to the server the following string to extract the value of the register: **AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%s**. Doing this on the server, the output will be: "AAAA.0804c000.ffffdcd8.0804930a.0804c060.f7eed483.0804c000.SSof{There_are_no_secrets_in_stack}"

So, the flag is "SSof{There_are_no_secrets_in_stack}"
