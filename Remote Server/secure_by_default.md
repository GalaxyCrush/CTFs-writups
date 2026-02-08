# Challenge `Secure By Default` writeup

- Vulnerability: Client-side verification
    - The client can change the value of a cookie and the server will verify this value. The server stores a client-side cookie that strores the username in B64.
  
- Where: On `user` cookie on client session storage on mustard.stt.rnl.tecnico.ulisboa.pt:25056

- Impact: By changing the user value, the attacker can change his username to admin in Base64 and have access to the service.


##  Steps to reproduce

1. Use the PoC script included in this repository.
2. The script:
   - Sends a GET requests to mustard.stt.rnl.tecnico.ulisboa.pt:25056 to verify the answer from the server
   - Sends a POST request with the information that is asked(username).
   - Verify then the content of the page
   - Parse `admin` to Base64
   - Set the cookie's value `user` to the Base64 `admin`.
   - Send a GET request to retrieve the admin web view and get the flag. 
  

[(POC)](Scripts/secure_by_design.py)
