#-*- coding: utf-8 -*-
import tweepy
import config

CA = config.CA
CS = config.CS
AT = config.AT
AS = config.AS

auth = tweepy.OAuthHandler(CA, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

def tweet(text):
    try:
        api.update_status(text)
        print("ツイートに成功しました")
    except:
        print("ツイートに失敗しました")

def follow(user_id):
    try:
        api.create_friendship(user_id)
        print("フォローに成功しました")
    except:
        print("フォローに失敗しました")

def follow_id(user_id):
    try:
        api.create_friendship(user_id)
        print("フォローに成功しました")
    except:
        print("フォローに失敗しました")

def bye_follow(user_id):
    try:
        api.destroy_friendship(user_id)
        print("フォローの解除に成功しました")
    except:
        print("フォローの解除に失敗しました")

def timeline(count):
    try:
        timeline = api.home_timeline(count=count, include_rts=False)
        for status in timeline:
            print("タイムラインの取得に成功しました")
            return status.text
    except:
        print("タイムラインの取得に失敗しました")
    
def serch(word, count):
    try:
        word = word
        count = count
        serch = api.search(q=word, count=count, include_rts=False)
        for status in (serch):
            #user_name = status.user.name
            #screen_id = status.user._json['screen_name']
            #tweet_id = status.id
            user_id = status.user.id
            print("検索に成功しました")
            return user_id
    except:
        print("検索に失敗しました")
def me():
    try:
        me = api.me()
        print("名前: " + me.name)
        print("@" + me._json['screen_name'])
        print("プロフィール: " + me.description)
        print("フォロー中: " + str(me.friends_count) + " フォロワー: " + str(me.followers_count))
    except:
        print("プロフィールの取得に失敗しました")

def FollowBack(): #自分がフォローされてるけどフォロー返してないやつ
    follower_id = api.followers_ids()
    follow_id = api.friends_ids()
    not_followed_user_id = set(follower_id + follow_id) ^ set(follow_id)

    for user_id in not_followed_user_id:
        try: 
            api.create_friendship(user_id)
        except Exception as e:
            print(e)
def FollowBack_unFollow(): #自分がフォローしてるけどフォロー返されてないやつ
    follower_id = api.followers_ids()
    follow_id = api.friends_ids()
    not_followed_user_id = set(follower_id + follow_id) ^ set(follower_id)

    for user_id in not_followed_user_id:
        try: 
            api.destroy_friendship(user_id)
        except Exception as e:
            print(e)