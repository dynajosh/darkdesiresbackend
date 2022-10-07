from cProfile import Profile
from itertools import count
import json
from django.shortcuts import render
import tweepy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Influencer
from .serializers import TweetIdSerializer
from drf_yasg.utils import swagger_auto_schema
import instaloader
# import selenium
# import time

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# actionChain = webdriver.ActionChains(driver)


from main import serializers


ig = instaloader.Instaloader()

@api_view(['POST'])
def testInstagram(request):
    ig.login("joshuaoriakhi", "CjXyHp9qJne")
    profile = instaloader.Profile.from_username(ig.context, 'clinton9979') 
    # post = instaloader.Profile
    post = instaloader.Post.shortcode_to_mediaid('CjYFaTaoGYO')
    influencers  = Influencer.objects.all()
    influencer_list = []
    likers = []
    print(post)

    # short_code = "CjXwbaIvphS"
    # def code_to_media_id(short_code):
    #     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    #     media_id = 0;
    #     for letter in short_code:
    #         media_id = (media_id*64) + alphabet.index(letter)

    #         print(media_id)
    #     return media_id
    # code_to_media_id(short_code)

    # for post in profile.get_posts():
    #     likes = post.get_likes()
    #     for likee in likes:
    #         id_com = likee.username
    #         print(id_com)
    #     # print(comments)

    # post = Post.from_mediaid(ig.context, 'CjXwbaIvphS')
    print("okay")


    # driver.get('https://www.instagram.com/p/BuE82VfHRa6/')

    # time.sleep(2)

    # userid_element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/div[2]/button').click()
    # time.sleep(2)



    # elems = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate TlrDj']")

    # users = []


    # for i in range(10):
    #     i += 1
    #     if(i%10) == 9 :
    #         driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div').click()
    #         actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

    #     print('/html/body/div[4]/div/div/div[2]/div/div/div['+str(i)+']/div[2]/div[1]/div/a')
    #     Title = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div['+str(i)+']/div[2]/div[1]/div/a').get_attribute('title')
    #     users.append(Title)
    #     print('Title : ' + Title)

    # print(users)

    # for post in profile.get_posts():
    #     counter = post.likes
    #     print(counter)
    #     # post_likes = post.get_likes()
        # print(post_likes)

        # post_comments = post.get_comments()
        # print(post_comments)
        # for likee in post_likes:
        #     print(likee.username)
        # print(post_likes)  # post_likes object
        # print(post_comments) # # post_comments object




    # for influencer in influencers:
    #     influencer_id = int(influencer.instagram_id)
    # influencer_list.append(influencer_id)
    # if influencer_id in likers:
    #     print("e dey there")
    #     influencer.rating += 10
    #     influencer.save()
    # else:
    #     print("e no dey")
    #     print(likers)
    #     print(influencer_list)

    # print(profile)
    return Response("okay")  



# USER = "fh"
# PROFILE = USER

# Create your views here.

consumer_key = ""
consumer_secret = ""


tweet_id = 1577284838104518657


client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAOIahwEAAAAAbKfYFaS3X5hq4kVUANay6Nwf0Co%3DTkJm9tivnt2bAEFSwE7BOBHgFsksKshrV926bwNRrRpSfOlWui")


@api_view(['GET'])
def getTweet(*args, **kwargs):
    response = client.get_tweets(tweet_id, tweet_fields=["text"])

    for tweet in response.data:
        print(tweet.id, tweet.text)

    return Response("okay")


@swagger_auto_schema(methods=['post'], request_body=TweetIdSerializer)
@api_view(['POST'])
def getLikingUsers(request):
    serializer = TweetIdSerializer(data=request.data)
    serializer.is_valid()
    data = serializer.validated_data
    response = client.get_liking_users(data['tweet_id'], user_fields=["profile_image_url", "id"])
    influencer_list = []
    likers = []

    # print(otweet_id)


    for liker in response.data:
        likers.append(liker.id)

    influencers  = Influencer.objects.all()

    for influencer in influencers:
        influencer_id = int(influencer.twitter_id)
        influencer_list.append(influencer_id)
        if influencer_id in likers:
            print("e dey there")
            influencer.rating += 10
            influencer.save()
        else:
            print("e no dey")
            print(likers)
            print(influencer_list)

    # print(likers, influencer_list)

    return Response("okay")