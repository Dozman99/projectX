from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'
# because "urlPattern" instead of "urlpattern"
urlpatterns = [   # shows the individual post
    # shows all the post
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
]
