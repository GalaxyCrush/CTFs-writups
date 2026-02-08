# Challenge `Python requests Again` writeup

- Vulnerability: Client-side verification
    - The client can change the value of a cookie and the server will verify this value.
  
- Where: On `remaining_tries` cookie on client session storage on mustard.stt.rnl.tecnico.ulisboa.pt:25054
  
- Impact: This allows the user to bypass the limitation of one trie per user defined by the web service, leanding to the user exploit the app and reach the goal per session.

##  Steps to reproduce

1. Use the PoC script included in this repository.
2. The script:
   - Sends a GET requests to mustard.stt.rnl.tecnico.ulisboa.pt:25054/hello to verify the answer from the server
   - Parses the banner to obtain the target ("until you get to X") and the current counter ("CURRENT = Y")
   - Update the cookie`remaining_tries` to 1 every request that is made so that we can repeat the requests.
   - Sends "MORE" repeatedly until current == target
   - Sends "FINISH" and prints the server response (flag)

[(POC)](Scripts/python_requests_again.py)
