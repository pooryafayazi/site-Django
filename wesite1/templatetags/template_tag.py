from django import template

register = template.Library()


from blog.models import Post


@register.filter
def truncate_w(text, word_count):
    words = text.split()
    if len(words) > word_count:
        return ' '.join(words[:word_count]) + '...'
    return text


@register.inclusion_tag('wesite1/least-post.html')
def least():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:6]    
    return {'posts' : posts}