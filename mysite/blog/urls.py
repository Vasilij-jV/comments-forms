from django.urls import path
from .views import *
from . import views

app_name = 'blog'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_id>/', post_share, name='post_share'),
    path('message_to_admin/', admin_share, name='admin_share'),
    path('latest_messages/', latest_messages, name='latest_messages'),
    path('article_list/', article_list, name='article_list'),
    path('<slug:slug>/', article_detail, name='article_detail'),
]
