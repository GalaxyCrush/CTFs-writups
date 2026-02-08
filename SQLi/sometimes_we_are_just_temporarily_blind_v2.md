# Challenge `Sometimes we are just temporarily blind - V2` Writeup

- Vulnerability: SQL Injection attack
- Where: Search blog posts text field
- Impact: Allows users to find hidden Databases in the system, leading to the discover of a secret.

Note: The challange logic is the same as the ones before this, but more work intensive, because now we have to discover the tables by the found matches on the search result.

## Steps to reproduce

The steps are the same as the previous challange.

[POC](POC/blind.py)