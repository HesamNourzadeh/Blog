from gtts import gTTS
from django.http import HttpResponse
import os
from django.shortcuts import render
from Blog.models import Post
def home(request):
    Posts = Post.objects.all()
    recent_post = Post.objects.all().order_by('-created','-updated')
    return render(request , "home_app/index.html" , {"Articles" : Posts })

