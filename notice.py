import time

from pynostr.key import PrivateKey
import requests
from win10toast import ToastNotifier

identity_pk = PrivateKey.from_nsec("nsec1hrgtl3j3mr3znnnx8zf6p0wxmn42vr0lem28l97r2djeteejfrwqu8pdjp")


def read():
    with open("count.txt", "w+") as file:
        val = file.read().strip()
        if val is None or val == "":
            val = 0
        file.write(str(val))
    return val

def write(val):
    with open("count.txt", "w+") as file:
        file.write(str(val))
    return val


while True:
    responses = requests.get("https://api-worker.noscription.org/indexer/balance?npub="+"npub1tqw79k35z2m0mhenun3lkrwcgtghn4k8huqywrmatneya3swhtls4wn3s4")
    data = responses.json()
    print(data)
    old = read()
    if data[0]['balance'] > old:
        toaster = ToastNotifier()
        toaster.show_toast("挖到了！！！", f"新增{data[0]['balance'] - old}个, 总量{data[0]['balance']}", duration=5)
        write(data[0]['balance'])
    time.sleep(10)


