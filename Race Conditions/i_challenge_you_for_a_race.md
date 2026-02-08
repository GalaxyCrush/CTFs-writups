# Challenge `I Challenge you for a Race` writeup

- Vulnerability: Race Condition on the transiction between `access()` and `fopen()`
  - **TOCTOU (Time-of-Check to Time-of-Use)**: This vulnerability arises when there is a time gap between the check of a resource's state (e.g., verifying permissions with `access()`) and its actual use (e.g., opening the file with `fopen()`). During this gap, we can manipulate the resource, leading to unintended behavior, in this case, read the file.

- Where: In the challenge's code, specifically in the sequence of operations where the program checks permissions (`access()`) and then opens the file (`fopen()`). This creates a window of opportunity for replacing the file being accessed.

- Impact: An attacker can exploit this vulnerability to trick the program into accessing or manipulating files that would normally be restricted. In this challenge, the goal is to access the `flag` file, which contains the CTF goal flag, but we have no read permissions.

## Steps to reproduce

1. The script creates a symbolic link (`$LINK`) that rapidly alternates between a dummy file (`dummy.txt`) and the target file (`../../challenge/flag`).
2. The `challenge` program is repeatedly executed attempting to access the symbolic link and with the `&` the code will "fork" and continue to the other symlink set.
3. Due to the race condition, there is a chance that the program accesses the target file (`flag`) when the symbolic link points to it.
4. If the exploit is successful, the `challenge` program will access the `flag` file, allowing to read the flag that is `SSof{Time_of_Check_Time_of_Use_or_toctou_racing_ftw}`

Note: The script works if it is executed on **tmp/aabbweirdaabb** and **fileSus.txt** and **dummy.txt** are in that directory. Besides the fact that the challange is on **~/challange/**

[(POC)](scripts/i_challenge_you.sh)