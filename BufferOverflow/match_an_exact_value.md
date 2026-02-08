# Challenge `Match an Exact Value` writeup

- Vulnerability: Buffer Overflow
- Where: In the buffer and test variables on the code besides the fact of the use of gets
- Impact: Allows to change variables beyond the buffer's memory, in this case the test variable.

## Steps to reproduce

1. Analyze the source code, and note that the buffer has a limit of 64 characters and the program uses `gets()` which does not validate input size.
2. To alter other variables, we need to overflow the buffer. We can implement a script that sends a string greater than 64 characters to alter the variable test.
3. In this case, we want to change the value of test to a specific value (`0x61626364`). The overflow part needs to be the value we want: `abcd` (where 0x61='a', 0x62='b', 0x63='c', 0x64='d'). However, since we are sending through the network and the architecture is little-endian, we need to reverse the byte order, so we send a string greater than 64 bytes and the extra part as `dcba`. 
4. Executing the script gives us the flag: `SSof{Buffer_Overflow_to_change_values_to_wh4t3v3r_you_want}`

- Note 1: Local variables are stored sequentially on the stack. In this case, `buffer[64]` is followed by the `test` variable. By sending 64 bytes, we completely fill the buffer, and the next 4 bytes overwrite the `test` variable.

- Note 2: x86/x64 systems use little-endian, meaning the least significant byte is stored first in memory. Therefore, to obtain `0x61626364`, we need to send the bytes in reverse order: `\x64\x63\x62\x61` (or "dcba").

[(POC)](POC/match_an_exact_value.py)