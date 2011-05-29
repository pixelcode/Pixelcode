from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime
from pixelcode.models import *
from models import *
from pixelcode.settings import MEDIA_URL
from django.contrib import messages

def index(request):
    posts = Post.objects.filter(publish=1)
    nav = Navigation.objects.get(slug='blog')
    
    context = { 'nav' : nav, 'posts' : posts, 'categories' : Category.objects.all() }    
    return render_to_response ( 'blog/index.html', context, context_instance = RequestContext(request))

def category_posts(request, category):
    category = Category.objects.get(slug=category)
    posts = Post.objects.filter(categories=category)
    nav = Navigation.objects.get(slug='blog')
    
    context = { 'nav' : nav, 'category' : category, 'posts' : posts, 'categories' : Category.objects.all() }
    return render_to_response ( 'blog/index.html', context, context_instance = RequestContext(request) )


def post(request, category, post):
    nav = Navigation.objects.get(slug='blog')
    
    from pixelcode.blog.forms import CommentForm
    posts = Post.objects.filter(slug=post)
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            from lushconcepts.blog.models import UserProfile
            from django.contrib.auth.models import User
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            comment = form.cleaned_data['comment']
            
            try:
                user = User.objects.get(username=name)
            except:
                user = User(username=name, email=email)
                user.save()
            try:
                userprofile = Userprofile(user=user, website=website)
            except:
                pass
            
            comment = Comment(title='User comment - '+post.title , content=comment, author=user, post=post, approve=0)
            comment.save()
            messages.add_message(request, messages.INFO, 'Thank you for the comment. It will be published on approval.', extra_tags='growl')
            form = CommentForm()
    else:
        form = CommentForm()
        
    category = Category.objects.get(slug=category)
    
    context = { 'nav' : nav, 'form' : form, 'posts' : posts, 'categories' : Category.objects.all() }
    
    return render_to_response (
        'blog/post.html',
        context,
        context_instance = RequestContext(request)
    )