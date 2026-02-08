# Challenge `Super Secure Lottery` Writeup

- Vulnerability: Buffer overflow
- Where: On the `read` on `run_lottery` function
  - The vulnerability exists because `read(0, guess, GUESS_SIZE)` reads 64 bytes into an 8-byte buffer, causing a buffer overflow that allows us to overwrite adjacent memory.
- Impact: Allows to change variable value

## Steps to reproduce

1. Analyzing the source code, we see that the win condition is when `memcmp(prize, guess, LOTTERY_LEN)` are equal.

2. Using GDB, we can determine the memory layout by checking the addresses with `p &guess` and `p prize`. The difference between these addresses gives us the offset of 0x30 (48 bytes) needed to reach the `prize` on the stack.

3. The strategy is to craft a payload where the first 8 bytes write a known value into `guess`, followed by 40 bytes (0x28) of padding to reach the `prize` pointer, and finally 8 bytes to overwrite the `prize` pointer to point back to the beginning of `guess`. This way, when `memcmp` compares `prize` with `guess`, it's actually comparing `guess` with itself, always resulting in a match.

4. Executing the script with this crafted payload gives us the flag: `SSof{You_will_NeVeR_guess_a_totally_random_lottery}`

[POC](POC/super_secure_lottery.py).