# Challenge `Pickles In a Seri(al)ous Race` writeup

- Vulnerability: Insecure Deserialization
  - The server uses the `pickle` module to deserialize user-controlled data without validation, allowing arbitrary code execution.

- Where: In the "Classy Note" mode of the server, specifically when reading notes.

- Impact: Exploiting this vulnerability allows an attacker to execute arbitrary commands on the server.

- NOTE: The server has two modes: "Classy" and "Free". The "Classy" mode is vulnerable to insecure deserialization, while the "Free" mode allows writing arbitrary files. A race condition between these modes can be exploited to execute the attack.

## Steps to reproduce

1. Generate a malicious payload that executes arbitrary commands.
2. Open two connections to the server:
   - Use the "Classy" mode in one connection to read the malicious note.
   - Use the "Free" mode in the other connection to write the malicious note.
3. Write the malicious note using the "Free" mode.
4. Read the malicious note using the "Classy" mode.
5. The server executes the malicious payload, leading to arbitrary command execution.
6. After the search on the server for a flag, it could be found on `home/ctf/flag` and doing `cat home/ctf/flag` the result was `SSof{It_is_alwasy_an_easy_race_with_Pickles_RCE}`

- Note: As we can execute arbitrary code on the server, we still need to look for the flag inside the server. One approach was doing multiple `ls` and analyze the results, but as i was trying, executing the bash and set the conection to interactive gave me access to the server, and what i did was search on the folder for something until i found a `home/ctf/flag` file. 

[(POC)](scripts/pickles.py)