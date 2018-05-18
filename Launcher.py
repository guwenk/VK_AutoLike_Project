import threading
from random import randint as rand
from time import sleep as wait
from datetime import datetime

import logger as log
import logo
import vklikeapi as vk

# https://oauth.vk.com/authorize?client_id=6457788&scope=wall&response_type=token
version = "5.74"
token = ""
group_id = ""
user_id = ""
update_rate = 40
delay_from = 15
delay_to = 40
min_likes = 1
big_delay_from = 160
big_delay_to = 600

fromid_group = int("-" + group_id)
vk.init(token, group_id, user_id)


# log.debug_on()


class Run(threading.Thread):
    def __init__(self):
        super(Run, self).__init__()
        self.stopped = False

    def run(self):
        logo.dodo()
        ur = update_rate
        while not self.stopped:
            if 1 > datetime.now().hour > 6:
                if ur == update_rate:
                    ur = 0
                    json_data = vk.Wall.get()
                    likes = vk.Wall.get_latest_post_likes(json_data)
                    fromid = int(vk.Wall.get_from_id(json_data))
                    post_id = vk.Wall.get_latest_post(json_data)
                    if not vk.Likes.is_liked(post_id):
                        if likes < min_likes:
                            if fromid_group == fromid:
                                delay = rand(delay_from, delay_to)
                                log.d("From dodo")
                            else:
                                delay = rand(big_delay_from, big_delay_to)
                                log.d("Not from dodo")
                            log.i("Delay = " + str(delay))
                            wait(delay)
                        else:
                            log.i("Delay = 0")
                        log.i_n(
                            "Likes = " + str(vk.Likes.add(post_id)) + "\n***Text***\n" + vk.Wall.get_latest_post_text(
                                json_data) + "\n**********")
            ur += 1
            wait(1)

    def stop(self):
        log.i("Exit. Please, wait...")
        self.stopped = True


print("Go to \nhttps://oauth.vk.com/authorize?client_id=6457788&scope=wall&response_type=token\n and copy text from "
      "\"access_token =\" to \"&\" not including")
token = input()
print("Enter group id (without \'-\')")
group_id = input()
print("Enter user id")
user_id = input()

r = Run()
r.start()

while 1:
    uin = input()
    if uin == "stop" or uin == "exit" or uin == "qqq" or uin == "q" or uin == "quit":
        r.stop()
        exit(0)
