## Challenge `Guess a BIG Number` writeup


- Vulnerability: Brute-force attack

- Where: The vulnerability is present on the endpoint **/number/{}**

- Impact: An attacker can determine the server's chosen number and retrieve the flag.

## Steps to reproduce

1. Observe the endpoint's responses when guessing numbers:
   - If the guess is lower than the secret number the server replies "Higher!"
   - If the guess is higher than the secret number the server replies "Lower!"
   - If the guess is correct the server returns the flag (or a success message)

2. Because the endpoint provides feedback about the value chosen, it acts as an oracle. It wil be usefull to use a binary search over the large known range (0–100000).

Algorithm (binary search)
- Initialize low = 0 and high = 100000.
- Repeat while low <= high:
  - mid = (low + high) // 2
  - Send GET /number/{mid}
  - If response contains "Higher!" then low = mid + 1
  - If response contains "Lower!" then high = mid - 1
  - If response indicates the flag then the secret number is mid;


[PoC link](Scripts/bignumbers.py)
