# Challenge `Python requests` writeup

- Vulnerability: Logic flaw / protocol brute-force;
  - The user can ask for unlimited MORE commands reaching the goal.
- Where: Overall service provided by mustard.stt.rnl.tecnico.ulisboa.pt:25053.
- Impact: This allows the user to only resend requests until he reaches the goal.

##  Steps to reproduce

1. Use the PoC script included in this repository.
2. The script:
   - Sends a GET requests to mustard.stt.rnl.tecnico.ulisboa.pt:25053/hello to verify the answer from the server
   - Parses the banner to obtain the target ("until you get to X") and the current counter ("CURRENT = Y")
   - Sends "MORE" repeatedly until current == target
   - Sends "FINISH" and prints the server response (flag)

[(POC)](Scripts/python_requests.py)
