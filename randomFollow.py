#-*- coding: utf-8 -*-
import twtr
import datetime
import time

def rndmFollow(words):
    try:
        user_id = twtr.serch(words, 1)
        twtr.follow(user_id)
    except:
        print("ランダムなフォローに失敗しました")