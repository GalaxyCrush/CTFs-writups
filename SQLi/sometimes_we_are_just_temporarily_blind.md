# Challenge `Sometimes we are just temporarily blind` Writeup

- Vulnerability: SQL Injection attack
- Where: Search blog posts text field
- Impact: Allows users to find hidden Databases in the system, leading to the discover of a secret.

Note: The challange logic is the same as the ones before this, but more work intensive, because now we have to discover the tables by the found matches on the search result.

## Steps to reproduce

1. We perform the same strategy as before, by inputting `%'`, which leads to the discovery of the query `SELECT id, title, content FROM blog_post WHERE title LIKE '%%'%' OR content LIKE '%%'%'`. However, now only the matching results are displayed.

2. To find the tables, we need to construct strings that match the names of tables existing in the system. For this, we can use a script with the following logic:
   1. Use the query `q' UNION SELECT tbl_name, type, NULL FROM 'sqlite_master' WHERE type='table' AND substr(tbl_name,1,{i}) == '{substring}'; --` to search the `sqlite_master` table for rows where the type is `table` and the name starts with the given substring. This is case sensitive due to use all the letters possible in ASCII including lower and uper case letters. The `{substring}` is the current substring that we are trying to match, and the `i` is the index that we are trying to make a substring of.
   2. The first step is to count how many tables exist in the `sqlite_master` table. To do this, iterate over the possible starting letters and note which ones return a result greater than zero.
   3. Next, for each table (using either an index or the starting letter), iterate over the letters to build the full name of each existing table, one character at a time.
   4. The result will be the existing tables, which are: `super_s_sof_secrets`, `blog_posts`, and `users`.

3. Now that we know the secret table, we need to discover its columns. To do this, we could use the query `q' UNION SELECT name, NULL, NULL FROM pragma_table_info('super_s_sof_secrets') WHERE substr(name,1,{index}) == '{substring}'; --`, which uses `pragma_table_info` to query information about the columns of the table `super_s_sof_secrets`.

4. The steps used to discover table names can be reused here, since the system behaves the same way. The result will be the columns of the table, namely `secret` and `id`.

5. Finally, we could use the query `q' UNION SELECT secret, NULL, NULL FROM 'super_s_sof_secrets' WHERE substr(secret,1,{index}) == '{substring}'; --` to display the content of the `secret` column, following the same strategy as above. The result will be the flag: `SSof{I_am_just_partially_blind_since_I_can_gEt_yoUr_datA_using_Boolean_Injections}`


[POC](POC/blind.py)