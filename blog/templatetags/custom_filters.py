from django import template
from blog.models import Post,Comment
register = template.Library()
from blog.models import Category
from django.utils import timezone
@register.filter
def truncate_w(text, word_count):
    words = text.split()
    if len(words) > word_count:
        return ' '.join(words[:word_count]) + '...'
    return text

 
@register.simple_tag
def get_latest_posts(count=6):
    return Post.objects.order_by('-created_date')[:count].filter(status=1, published_date__lte=timezone.now())

@register.inclusion_tag('blog/blog-latest_posts.html')
def latest_post(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts' : posts}


@register.simple_tag(name='comments_count')
def function(post_id):
    return Comment.objects.filter(post=post_id, approved=True).count()

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories' : cat_dict}
