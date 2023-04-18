from django.urls import path
from . import views   # user/views 불러오기

urlpatterns = [
    path('mypage/', views.mypage_list,name='mypage-list'),
    path('mypage_follower_list/', views.follower_view,name='follower-list'),
    path('mypage_following_list/', views.following_view,name='following-list'),

]
