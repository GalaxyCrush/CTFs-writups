import requests
import re

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25053 

link = f"{SERVER}:{PORT}"

# Create a session to persist the cookies between requests
s = requests.Session()

r = s.get(link + "/hello")
text = r.text

target = int(re.search(r"your target (\d+)", text, re.IGNORECASE).group(1))
current = int(re.search(r"Your current value is:\s*(\d+)", text, re.IGNORECASE).group(1))

print(f"Target: {target}, Current: {current}")

def parse_more(text):
    have = int(re.search(r"Here you have:\s*([-]?\d+)", text).group(1))
    target = int(re.search(r"Your target is:\s*(\d+)", text).group(1))
    current = int(re.search(r"Your current value is:\s*(\d+)", text).group(1))
    return have, target, current


while current != target:
    r = s.get(link + "/more")
    text = r.text

    if "Here you have" not in text:
        print("Cookies problem")
        break

    have, target, current = parse_more(text)
    print(f"Recebido: {have} | Current: {current} | Target: {target}")

if current == target:
    r = s.get(link + "/finish")
    print("\nFLAG:")
    print(r.text)

# O que foi feito, vi como as respostas do servidor estavam a ser recebidas, dei parse manualmente da string para ter os valores
# Guardei os valores do site.
# No fim, printei o resultado da página quando cheguei ao valor com finish.
# Não preciso de mais nada pois o session já guarda as cookies nesta sessão, logo este script funciona para uma sessão individual.