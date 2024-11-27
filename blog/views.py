from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
def blog_view(request):
    posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context=context)


"""def blog_single_(request):
    posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())[0]
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html', context=context)"""

def blog_single(request, post_id):
    posts = get_object_or_404(Post,status=1, id = post_id)    
    posts.counted_views += 1
    posts.save()
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html', context=context)


