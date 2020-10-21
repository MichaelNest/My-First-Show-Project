from django.urls import path
from .views import ArticleListView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView, ArticleCreateView, article_my_list

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('my_articles', article_my_list, name='article_my_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]