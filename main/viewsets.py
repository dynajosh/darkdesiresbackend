from .serializers import PostSerializer, InfluencerSerializer, CompanySerializer
from .models import Post, Influencer, Company
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class InfluencerViewset(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = InfluencerSerializer
    queryset = Influencer.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination


class CompanyViewset(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = CompanySerializer
    queryset =  Company.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination


class PostViewset(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = PostSerializer
    queryset =  Post.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination
