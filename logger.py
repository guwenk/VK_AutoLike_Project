from datetime import datetime

import telegrambot as notif

isDebug = False


def d(msg):  # debug
    if isDebug:
        print(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [D] " + str(msg))


def i(msg):  # info
    print(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [I] " + str(msg))


def d_n(msg):  # debug
    print(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [D] " + str(msg))
    notif.send(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [D]\n" + str(msg))


def i_n(msg):  # info
    print(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [I] " + str(msg))
    notif.send(datetime.strftime(datetime.now(), "[%Y.%m.%d %H:%M:%S]") + " [I]\n" + str(msg))


def debug_on():
    global isDebug
    isDebug = True


def debug_off():
    global isDebug
    isDebug = False
