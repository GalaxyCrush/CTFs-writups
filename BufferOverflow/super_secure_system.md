# Challenge `Super Secure System` writeup

- Vulnerability: Buffer Overflow
- Where: On the `strcpy` function because we are passing a 64 byte string to a buffer that is only 32 bytes long, without verifying the length.
- Impact: We could change the return address of the function, to execute the line that we want to execute after the retun, in this case the "Welcome back ..."

## Steps to reproduce

1. Analysing the source code we can identify the vulnerability in `strcpy()` which copies data into a 32-byte buffer without size validation.
 
2. Debug the binary in GDB and set a breakpoint at the check_password function to examine the stack layout.

3. Find the memory address where the buffer starts by inspecting the buffer variable address.

4. Examine the stack frame to locate where the saved ebx register value is stored on the stack.

5. Calculate the offset between the buffer start address and the saved ebx location by subtracting these addresses to determine how many bytes are needed to reach it.

6. Read and record the original values of the saved ebx and ebp registers from the stack, as these must be preserved to prevent the program from crashing.

7. Disassemble the main function to find the address of the instruction that prints the flag, which comes after the check_password call and bypasses the if condition verification.

8. Construct the payload by concatenating: padding bytes to fill up to saved ebx, the original ebx value, the original ebp value, and finally the modified return address pointing to the flag-printing instruction.

9. Send the crafted payload which will overflow the buffer and overwrite the return address on the stack.

10. When check_password returns, the CPU reads the modified return address from the stack and jumps directly to the flag-printing code, completely bypassing the password verification and outputing the flag `SSof{Jump_to_wherever_you_want}`


[(POC)](POC/super_secure_system.py)