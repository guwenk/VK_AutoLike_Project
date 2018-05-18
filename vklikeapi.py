import json

import requests

import logger as log

version = "5.74"
token = None
group_id = None
user_id = None
isInitialized = False


def init(vk_token, vk_group_id, vk_user_id):
    global token
    global group_id
    global user_id
    global isInitialized
    token = vk_token
    group_id = vk_group_id
    user_id = vk_user_id
    isInitialized = True
    return True


def get_response(url, log_tag):  # returns txt json
    k = 1
    while k <= 3:
        try:
            log.d(log_tag + " try " + str(k) + "/3")
            response = requests.get(url).text
            log.d(log_tag + " complete")
            k = 111
            return response
        except Exception:
            k += 1
            log.d(log_tag + " error")
    try:
        f = open("stub.json")
        stub = f.read()
        f.close()
        return stub
    except Exception:
        for i in range(3):
            log.d_n("FUUUUUUUUCK!!!!!!!!")


class Likes:
    def add(post_id):  # returns likes count
        return json.loads(get_response(
            "https://api.vk.com/method/likes.add?type=post&owner_id=-" + str(group_id) + "&item_id=" + str(
                post_id) + "&v=" + version + "&access_token=" + str(token), "VK.Like.Add"))["response"]["likes"]

    def is_liked(post_id):  # returns bool
        return json.loads(get_response(
            "https://api.vk.com/method/likes.isLiked?user_id=" + str(user_id) + "&type=post&owner_id=-" + str(group_id) + "&item_id=" + str(
                post_id) + "&v=" + version + "&access_token=" + str(token), "VK.Like.isLiked"))["response"]["liked"] == 1


class Wall:
    @staticmethod
    def get():  # returns json
        return json.loads(get_response(
            "https://api.vk.com/method/wall.get?owner_id=-" + str(group_id) + "&v=" + version + "&count=" + str(
                2) + "&access_token=" + str(token), "VK.Wall.Get"))

    def get_latest_post(wall_json):
        if wall_json["response"]["items"][0]["date"] > wall_json["response"]["items"][1]["date"]:
            return wall_json["response"]["items"][0]["id"]
        return wall_json["response"]["items"][1]["id"]

    def get_latest_post_text(wall_json):
        if wall_json["response"]["items"][0]["date"] > wall_json["response"]["items"][1]["date"]:
            return wall_json["response"]["items"][0]["text"]
        return wall_json["response"]["items"][1]["text"]

    def get_latest_post_likes(wall_json):
        if wall_json["response"]["items"][0]["date"] > wall_json["response"]["items"][1]["date"]:
            return wall_json["response"]["items"][0]["likes"]["count"]
        return wall_json["response"]["items"][1]["likes"]["count"]

    def get_from_id(wall_json):
        if wall_json["response"]["items"][0]["date"] > wall_json["response"]["items"][1]["date"]:
            return wall_json["response"]["items"][0]["from_id"]
        return wall_json["response"]["items"][1]["from_id"]
