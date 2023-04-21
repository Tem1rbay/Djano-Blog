from django.urls import path, include
from . import views
from articles import views as articles_views


app_name = 'blog'

urlpatterns = [
    path('articles/', include('articles.urls',
                              namespace='articles'), name='articles'),
    path('accounts/', include('accounts.urls',
                              namespace='accounts'), name='accounts'),
    path('', articles_views.articles_list, name='index'),
    path('aboutUs/', views.whoAmI, name='aboutUs'),
]
