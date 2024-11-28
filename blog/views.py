from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    posts = Post.objects.filter(status=1 , published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context=context)


def blog_single(request, post_id):
    current_post = get_object_or_404(Post,status=1, id = post_id)    
    current_post.counted_views += 1
    current_post.save()

    all_posts = Post.objects.all().order_by('published_date')    
    current_index = list(all_posts).index(current_post)
    previous_post = all_posts[current_index - 1] if current_index > 0 else None
    next_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None
    context = {
        'current_post': current_post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    
    return render(request, 'blog/blog-single.html', context)

