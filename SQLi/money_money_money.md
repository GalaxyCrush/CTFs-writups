# Challenge `Money, money, money!` Writeup

- Vulnerability: SQL injection
- Where: On the Profile Bio textfield
- Impact: It can be used to perform SQL manipulation, in this case we could perform SQL queries to alter the tokens needed for the jackpot.

## Steps to Reproduce

1. In the bio text field, we know we can inject SQL queries (see notes). We also know the full query being used is an UPDATE statement, which means we can change database values with the correct input.
2. In the previous challenge, we noted that each user has a `jackpot_val` column, which is the number of tokens needed for the jackpot. We can set this value to `0` to get the jackpot immediately. The payload would be `',jackpot_val='0`, which appends the `jackpot_val` update to the `bio` update. The resulting query will be: `UPDATE user SET bio = '', jackpot_val='0' WHERE username = 'simsim'`.
3. As a result we get the jackpot, which is the flag: `SSof{Can_you_UPDATE_your_tokens}`.

- Note: If you enter `'something`, it will break the query and show the following error message: `(sqlite3.OperationalError) near "something": syntax error [SQL: UPDATE user SET bio = ''something' WHERE username = 'simsim']`. This happens because your input closes the `bio=` part of the query, and the rest is interpreted as invalid SQL, exposing the full query in the error.

