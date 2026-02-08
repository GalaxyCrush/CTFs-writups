# Challenge `Another Jackpot` writeup

- Vulnerability: Race Condition
  - There is a gap between code execution when logging in, the server commits the username without verifying the password. This give us a period where we are the user that we wrote.  
- Where: Is on the `/login` and `/jackpot` endpoints
  - The backend operation of login sets the server state username as the username passed in the login box without the validation of the password. And there is a verification that compares if username is equal to `admin`, and if true the jackpot can hit if not will never hit. So, in theory we could do `/jackpot` while the `login` is in execution and hit the jackpot because in a moment we were the `admin`. 
- Impact: This give us a period where we can be a user that we write in the `username` field, and as i mentioned earlir, exploit the `/jackpot` endpoint.


## Steps to reproduce

1. Analyze the server code and see the vulnerability discibed above
2. Create a Session to maintain cookies.
3. Make two tasks at the same time(i used threads to paralilize the flow)
   - Spamming the `/login` to exploit the vulnerability
   - Spamming the `/jackpot` to try gather the flag while we are the admin.
4. In the prints of the script, some prints will be normal prints where nothing important happend, but some of them, if all went ok, will be the html with the flag, that is `SSof{There_was_never_an_admin_user}`.

[(POC)](scripts/another_jackpot.py)