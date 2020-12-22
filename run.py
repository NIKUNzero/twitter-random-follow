#-*- coding: utf-8 -*-
import tweepy
import config
import twtr
import randomFollow
import time
import schedule
import sys
import datetime

CA = config.CA
CS = config.CS
AT = config.AT
AS = config.AS

auth = tweepy.OAuthHandler(CA, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)
def run():
    print("プログラムを開始しますか？ [Y/n]")
    eula = input()
    if "y" == eula or "Y" == eula or "ｙ" == eula:
        while True:
            try:
                randomFollow.rndmFollow("検索ワード")
                time.sleep(10)
                randomFollow.rndmFollow("検索ワード")
                time.sleep(10)
                randomFollow.rndmFollow("検索ワード")
                time.sleep(10)
                randomFollow.rndmFollow("検索ワード")
                time.sleep(10)
                randomFollow.rndmFollow("検索ワード")
                time.sleep(60)
                randomFollow.rndmFollow("検索ワード")
                time.sleep(60)
                randomFollow.rndmFollow("検索ワード")
                time.sleep(10)
                print("-----Profile-----")
                twtr.me()
                print("-----------------")
                time.sleep(3600)
            except Exception as e:
                print("エラーが発生しました")
                print(e)
                time.sleep(14400)
    else:
        print("同意を確認することができませんでした")
        print("プログラムを終了します。")
        sys.exit()

run()
