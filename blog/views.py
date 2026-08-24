from django.shortcuts import render
from .models import Post



def post_list(request):
    posts = posts.objects.all()
    return render(request, 'home.html', {'posts': posts})


