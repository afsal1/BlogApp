"""SocialMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SocialMediaApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name="home page"),
    path('signup/', signupview, name="signup view"),
    path('', loginview, name="login view"),
    path('find_people/', find_people, name="find people"),
    path('send_friend_request/<int:userid>/',
         send_friend_request, name="send friend request"),
    path('accept_friend_request/<int:requestid>/',
         accept_friend_request, name="accept friend request"),
    path('confirm_accept_request/',
         confirm_accept_request, name="confirm accept friend request"),
    path('logout/', logout, name="logout"),
    path('show_friends/', show_friends, name="show_friends"),
    path('upload_image_to_feed/', upload_image_to_feed, name="upload_image_to_feed"),
    path('upload_videos_to_feed/', upload_videos_to_feed, name="upload_videos_to_feed"),
    path('my_video_feed/', my_video_feed, name="my_video_feed"),
    path('my_image_feed/', my_image_feed, name="my_image_feed"),
    
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
