from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User, FriendRequest, ImageMedia, VideoMedia
from django.contrib import messages


def homepage(request):
    """
        Function Name: homepage
        Description: show the home page of the App
        Return: list of feeds of the friends

    """
    user = request.user.id
    friends = User.objects.filter(friends=request.user).first()
    image_feeds = ImageMedia.objects.filter(friend=friends)
    video_feed = VideoMedia.objects.filter(friend=friends)

    context = {
        'image_feeds': image_feeds,
        'video_feed': video_feed
    }
    return render(request, 'Homepage.html', context)


def signupview(request):
    """
        Function Name: signupview
        Description: Signup to access the site
        Return: user info

    """
    if request.method == 'POST':

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_2 = request.POST.get("password_2")
        if password == password_2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return HttpResponseRedirect(request.path_info)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return HttpResponseRedirect(request.path_info)
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return HttpResponseRedirect(request.path_info)

    else:
        return render(request, 'Signup.html')


def loginview(request):
    """
        Function Name: loginview
        Description: login to access the site
        Return: user info

    """

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/homepage/')
        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def find_people(request):
    """
        Function Name: find_people
        Description: search for new friends
        Return: registered user details

    """
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'find_people.html', context)


@login_required
def send_friend_request(request, userid):
    """
        Function Name: send_friend_request
        Description: find new friends by sending request
        Return: http response

    """
    from_user = request.user
    to_user = User.objects.get(id=userid)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request already sent')


@login_required
def accept_friend_request(request, requestid):
    """
        Function Name: accept_friend_request
        Description: adding new friends by accepting request
        Return: http response

    """
    friend_request = FriendRequest.objects.get(id=requestid)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request Accepted')
    else:
        return HttpResponse('friend request not Accepted')


def confirm_accept_request(request):
    """
        Function Name: confirm_accept_request
        Description: to list all friend requests
        Return: list of friend requests

    """
    friend_request = FriendRequest.objects.filter(to_user=request.user)
    context = {
        'friend_request': friend_request,
    }
    return render(request, 'accept_request.html', context)


def show_friends(request):
    """
        Function Name: show_friends
        Description: to list all the friends
        Return: list of all friends

    """
    friends = User.objects.filter(friends=request.user)
    context = {
        'friends': friends,
    }
    return render(request, 'show_friends.html', context)


def upload_image_to_feed(request):
    """
        Function Name: upload_image_to_feed
        Description: adding new images to the feed
        Return: return to my feed

    """
    if request.method == 'POST':
        title = request.POST["title"]
        image = request.FILES['image']
        friend = request.user
        feed = ImageMedia.objects.create(
            title=title, image=image, friend=friend)

        return redirect('/my_image_feed/')
    else:
        return render(request, 'upload_image_feeds.html')


def upload_videos_to_feed(request):
    """
        Function Name: upload_videos_to_feed
        Description: adding new videos to the feed
        Return: return to my feed

    """
    if request.method == 'POST':
        title = request.POST["title"]
        video = request.FILES['video']
        friend = request.user
        feed = VideoMedia.objects.create(
            title=title, video=video, friend=friend)

        return redirect('/my_video_feed/')
    else:
        return render(request, 'upload_video_feeds.html')


def my_image_feed(request):
    """
        Function Name: my_feed
        Description: to show the images added by the user
        Return: all the feeds of the user

    """
    if request.method == 'GET':
        feed = ImageMedia.objects.filter(friend=request.user.id)
        context = {
            'my_feed': feed
        }
        return render(request, 'my_image_feed.html', context)


def my_video_feed(request):
    """
        Function Name: my_feed
        Description: to show the videos added by the user
        Return: all the feeds of the user

    """
    if request.method == 'GET':
        feed = VideoMedia.objects.filter(friend=request.user.id)
        context = {
            'my_feed': feed
        }
        return render(request, 'my_video_feed.html', context)


def logout(request):
    """
        Function Name: logout
        Description: to logout from the site 
        Return: login page

    """
    auth.logout(request)
    return redirect("/")
