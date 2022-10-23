from pyexpat import model
from urllib import response
from .models import Post
from rest_framework import serializers
import random


class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        gradient_list = [
        {
            "primary" : "#73c8a9",
            "secondary" : "#373b44"
        },
        {
            "primary" : "#485563",
            "secondary" : "#29323c"
        },
        {
            "primary" : "#52c234",
            "secondary" : "#061700"
        },
        {
            "primary" : "#70e1f5",
            "secondary" : "#ffd194"
        },
        {
            "primary" : "#f0c27b",
            "secondary" : "#4b1248"
        },
        {
            "primary" : "#ff4e50",
            "secondary" : "#f9d423"
        },
        {
            "primary" : "#215f00",
            "secondary" : "#e4e4d9"
        },
        ]
        
        new_post = Post()
        new_post.body = validated_data["body"]
        gradient_item = random.randint(0, int(len(gradient_list)))
        print(gradient_item)
        new_post.primaryColor = gradient_list[gradient_item].get("primary")
        new_post.secondaryColor = gradient_list[gradient_item].get("secondary")

      
        new_post.save()

        return new_post

    class Meta:
        fields = "__all__"
        model = Post

