from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post,Comment
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def blog_view(request,**kwargs): 
#def blog_view(request,cat_name=None,author_username=None):
    posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())
    if kwargs.get('cat_name') is not None:
    #if cat_name:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
    #if author_username:
        posts = posts.filter(author__username =kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
    #if tag_name:
        posts = posts.filter(tags__name=kwargs['tag_name'])
    posts = Paginator(posts,3)

    
    #comments = Comment.objects.filter(approved=True)
    
    try:        
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context=context)


def blog_single(request, post_id):
    if request.method == 'POST':
        current_post = get_object_or_404(Post,status=1, id = post_id) 
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your comment is saved!")
        else:
            messages.add_message(request, messages.ERROR, "Your comment is NOT saved!")

    
    current_post = get_object_or_404(Post,status=1, id = post_id)    
    current_post.counted_views += 1
    current_post.save()

    all_posts = Post.objects.all().order_by('published_date').filter(status=1, published_date__lte=timezone.now())
    current_index = list(all_posts).index(current_post)
    previous_post = all_posts[current_index - 1] if current_index > 0 else None
    next_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None
    comments = Comment.objects.filter(post_id =current_post.id,approved=True)

    form = CommentForm()
    context = {
        'current_post': current_post,
        'previous_post': previous_post,
        'next_post': next_post,
        'comments' : comments,
        'form' : form,
    }
    if not current_post.login_require:        
        return render(request, 'blog/blog-single.html', context)
    else:
        if not request.user.is_authenticated:         
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            return render(request, 'blog/blog-single.html', context)
        

def blog_search(request):
    posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())  
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context=context)
