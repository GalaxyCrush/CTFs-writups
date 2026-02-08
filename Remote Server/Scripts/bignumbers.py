import requests

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25052 

link = f"{SERVER}:{PORT}"

# Create a session to persist the cookies between requests
s = requests.Session()

# Access the first link to set the user cookie
s.get(link)

r = s.get(link + "/number/0")
print(r.text)
r = s.get(link + "/number/100000")
print(r.text)

low, high = 0, 100000

while low <= high:
    mid = (low + high) // 2
    r = s.get(link + f"/number/{mid}")
    response = r.text

    if "Higher!" in response:
        low = mid + 1
    elif "Lower!" in response:
        high = mid - 1
    else:
        print("Number:", mid)
        print(response)
        break