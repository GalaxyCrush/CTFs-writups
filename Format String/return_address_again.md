# Challenge `Calling Functions Again` Writeup

- Vulnerability: Format String Vulnerability
- Where: On the printf function on the vuln() function
- Impact: It allows to the user to write in the arbitrary memory, namely override the function return call(eip) after the print function.

## Steps to reproduce

1. By sending format specifiers like %p or %x, it is possible to leak values from the stack. The first leaked value corresponds to an address inside the current stack frame of vuln(). This leaked address is not the return address itself, but it is located at a known offset from it.

2. Through local analysis with GDB, it can be observed that the saved return address is located 144 bytes above the leaked stack address.

3. Since "**\%hhn**" writes only one byte at a time (mod 256), the return address is written byte‑by‑byte.

4. The address of win() is split into four bytes (little‑endian order). A character counter is maintained, and padding is calculated so that each "**\%hhn**" writes the correct byte value to memory, taking into account the mod 256 behavior.

5. After sending the crafted payload, the saved return address is overwritten. When vuln() returns, execution jumps directly to win(), printing the flag, that is: "SSof{returning_to_the_same_old_things}"

[(POC)](POC/return_address_again.py)
