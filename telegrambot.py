import threading
from datetime import datetime

import requests

tg_msg = ""
proxy = "137.74.254.242:3128"
proxies = {
    "http": proxy,
    "https": proxy
}


class Run(threading.Thread):
    def __init__(self, msg):
        super(Run, self).__init__()
        self.msg = msg
        self.k = 1

    def run(self):
        tid = getid()
        while self.k <= 10:
            print(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [I] " + "Telegram.send №" + str(
                tid) + " try " + str(self.k) + "/10")
            try:
                requests.get(tg_msg + self.msg, proxies=proxies)
                self.k = 111
                print(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [I] " + "Telegram message №" + str(
                    tid) + " delivered")
            except Exception:
                self.k += 1
                print(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [E] " + "Telegram.send №" + str(
                    tid) + " error")


def send(msg):
    if tg_msg != "":
        r = Run(msg)
        r.start()


def getid():
    try:
        getid.k += 1
    except AttributeError:
        getid.k = 0
    return getid.k
