from django.contrib import admin
from .models import Post, Influencer, Company

# Register your models here.
admin.site.register(Post)
admin.site.register(Influencer)
admin.site.register(Company)