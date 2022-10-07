from pyexpat import model
from urllib import response
from .models import Post, Influencer, Company
from rest_framework import serializers
import tweepy
import instaloader

twitter_client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAOIahwEAAAAAbKfYFaS3X5hq4kVUANay6Nwf0Co%3DTkJm9tivnt2bAEFSwE7BOBHgFsksKshrV926bwNRrRpSfOlWui")

instagram_client = instaloader.Instaloader()


    
    # profile = ig.load_profile_id("joshuaoriakhi")
    # fuck = str(profile)


    # print(profile)
    # return Response("okay")  


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Post


class InfluencerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        twitter_id = twitter_client.get_user(username=validated_data['twitter_username'])
        instagram_id = instagram_client.load_profile_id(validated_data['instagram_username'])
        print(instagram_id)

        new_influencer = Influencer()
        new_influencer.twitter_username= validated_data['twitter_username']
        new_influencer.instagram_username= validated_data['instagram_username']

        new_influencer.twitter_id = twitter_id.data.id
        new_influencer.instagram_id=instagram_id
        new_influencer.save()

        return new_influencer

    class Meta:
        fields = "__all__"
        model = Influencer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Company


class TweetIdSerializer(serializers.Serializer):
    tweet_id = serializers.IntegerField()

    class Meta:
        field = (
            "tweet_id",
        )
