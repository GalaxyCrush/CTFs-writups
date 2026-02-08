# Challenge `Simple Overflow` writeup

- Vulnerability: Buffer Overflow
- Where: In the buffer and tests variables on the code besides the fact of the use of gets
- Impact: Allows to change variables pass the memory of the buffer, in this case the test.

## Steps to reproduce

1. Analyze the source code, and note that the buffer has a limit of 128 characters.
2. To alter other variables, we need to overflow the buffer, to do that we can implement a script that sends a string greater that 128 char to alter the variable.
3. Executing the script, give us the flag that is `SSof{Buffer_Overflow_to_control_local_variables}`

- Note 1: Local variables are stored sequentially on the stack. In this case, `buffer[128]` is followed by the `test` variable. By sending 128 bytes, we completely fill the buffer, and the next bytes overwrite the `test` variable.

[(POC)](POC/simple_overflow.py)