from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User, Feeds
from django.contrib import messages


def homepage(request):
    """
        Function Name: homepage
        Description: show the home page of the App
        Return: list of feeds of the friends

    """
    user = request.user.id
    # friends = User.objects.filter(friends=request.user).first()
    image_feeds = Feeds.objects.all()

    context = {
        'image_feeds': image_feeds,
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


def upload_feed(request):
    """
        Function Name: upload_image_to_feed
        Description: adding post to the feed
        Return: return to my feed

    """
    if request.method == 'POST':
        title = request.POST["title"]
        tags = request.POST["tags"]
        content = request.POST["content"]
        category = request.POST['category']
        feed = Feeds.objects.create(
            title=title, category=category, tags=tags,
            content=content )

        return redirect('/all_feeds/')
    else:
        return render(request, 'upload_post.html')


def all_feeds(request):
    """
        Function Name: my_feed
        Description: to show the feeds added by the user
        Return: all the feeds of the user

    """
 
    feed = Feeds.objects.all()
    context = {
        'my_feed': feed
    }
    return render(request, 'all_feeds.html', context)



def filtered_feeds(request):
    """
        Function Name: filtered_feeds
        Description: to show the filtered_feeds
        Return: filtered_feeds 

    """
 
    category = category = request.POST['category']
    all_feed = Feeds.objects.all()
    
    if category == "blog":
        blog_feed = Feeds.objects.filter(category=category)
        context = {
            'my_feed': blog_feed
        }
        return render(request, 'filtered_feeds.html', context)
    elif category == "travel":
        travel_feed = Feeds.objects.filter(category=category)
        context = {
            'my_feed': travel_feed
        }
        return render(request, 'filtered_feeds.html', context)
    elif category == "other":
        other_feed = Feeds.objects.filter(category=category)
        context = {
            'my_feed': other_feed
        }
        return render(request, 'filtered_feeds.html', context)
    else:
        context = {
            'my_feed': all_feed
        }
        return render(request, 'filtered_feeds.html', context)


def logout(request):
    """
        Function Name: logout
        Description: to logout from the site 
        Return: login page

    """
    auth.logout(request)
    return redirect("/")
