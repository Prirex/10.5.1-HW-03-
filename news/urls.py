from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:id>/', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/create/', PostCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
]