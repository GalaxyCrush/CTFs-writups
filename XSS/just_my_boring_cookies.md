# Challenge `Just my boring cookies` Writeup

- Vulnerability: Reflected XSS attack

- Where: On the blog post search bar

- Impact: It allows to inject code that will be executed in the client browser. With this, we can use javascript, for example, to gather information about the cookied or to trigger a alert.

## Steps to reproduce

1. Do a script to gather the user cookies(`<script>alert(document.cookie)</script>`)
2. Execute the code by sending the code on the blog post search bar
3. The result will be an alert box with the cookie info that has the flag: `SECRET="SSof{USERS_HAVE_NO_SECRETS}"`