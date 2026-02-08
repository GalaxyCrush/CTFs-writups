# Challenge `I will take care of this site` Writeup

- Vulnerability: SQL Injection
- Where: On the Password text field 
- Impact: It let us login without the need of the correct password for that username.

## Steps to reproduce

1. On the `login` field, enter `admin'; --`, this what will do is that we enter a username, and all the query after the username verification will be commented, nullifying the password verification part (see notes).
2. On the `password` field, enter something that is non empty. The content is not important, because the password will not be needed for the SQL query.
3. Now, we are logged in on the admin account and the flag is in the profile, and the flag is `SSof{SQLi_on_SELECT_allows_you_to_become_an_administrator}`

- Note: Doing `'admin` will break the query, and present us with the following error message `(sqlite3.OperationalError) near "admin": syntax error [SQL: SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = ''admin' AND password = '961b6dd3ede3cb8ecbaacbd68de040cd78eb2ed5889130cceb4c49268ea4d506'] (Background on this error at: https://sqlalche.me/e/14/e3q8)`. The error is due to the fact that the string that we used as input will end the `username=` part of the query, and the admin string will be part of the query itself, presenting so the error exposing the full Query.



