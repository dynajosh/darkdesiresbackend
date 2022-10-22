from .serializers import PostSerializer
from .models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 50


class PostViewset(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = PostSerializer
    queryset =  Post.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination
