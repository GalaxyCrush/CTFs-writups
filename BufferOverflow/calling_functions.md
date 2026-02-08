# Challenge `Calling Functions` writeup

- Vulnerability: Buffer Overflow
- Where: In the buffer and fp variables on the code besides the fact of the use of gets.
- Impact: Allows to change variables pass the memory of the buffer, in this case the fp.

## Steps to reproduce

1. Analyze the source code, and note that the buffer has a limit of 32 characters.
2. To alter other variables, we need to overflow the buffer, to do that we can implement a script that sends a string greater that 32 char to alter the variable.
3. The fp is a function call, so what we need to to prior to send something to the server, is execute the program and verify using gdb in which memory address the `win` function is located at, and after the analysis it is located on `0x80486f1`
4. We send this value to the client, and then the `win` function is executed.
5. Executing the script, give us the flag that is `SSof{Buffer_Overflow_can_also_change_function_pointers}`

- Note 1: Local variables are stored sequentially on the stack. In this case, `buffer[32]` is followed by the `fp` variable. By sending 32 bytes, we completely fill the buffer, and the next bytes overwrite the `fp` variable.

[(POC)](POC/functions.py)