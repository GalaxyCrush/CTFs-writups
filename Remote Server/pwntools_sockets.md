## Challenge `PwnTools Sockets` writeup

- Vulnerability: Logic flaw / protocol brute-force. The user can ask for unlimited MORE commands reaching the goal.

- Where: Overall service provided by mustard.stt.rnl.tecnico.ulisboa.pt:25055 using TCP.

- Impact: An attacker can advance the counter that is supposed to be a sum of values indefinetly, reaching to the pretended values.


##  Steps to reproduce
1. Use the PoC script included in this repository.
2. The script:
   - Connects to mustard.stt.rnl.tecnico.ulisboa.pt:25055
   - Parses the banner to obtain the target ("until you get to X") and the current counter ("CURRENT = Y")
   - Sends "MORE" repeatedly until CURRENT == target
   - Sends "FINISH" and prints the server response (flag)

[PoC](Scripts/PwnTools_Sockets.py)