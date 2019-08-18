from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse # no need for this because we're rendering


# let's see for example what happens when we pass in some JSON
posts = [
    {
        'author':'Sam',
        'title': 'Post 1',
        'content': 'Some blog content',
        'date_posted':'August 17th, 2019'
    },
    {
        'author':'John',
        'title': 'Post 2',
        'content': 'Some other blog content',
        'date_posted':'August 17th, 2019'
    }
]

# home function handles what the user will see when we want to send her home
# urls.py is where we'll map these views functions to handle those url patterns
#     when requested

# don't forget to point these to and load in our templates
def home(request):
    context = {
        'posts':Post.objects.all()
        }
    return render(request,
                  'blog/home.html',
                  context)

def about(request):
    return render(request,
                  'blog/about.html',
                  {'title': 'About'})
