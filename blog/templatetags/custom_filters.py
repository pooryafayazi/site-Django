from django import template

register = template.Library()


@register.filter
def truncate_w(text, word_count):
    words = text.split()
    if len(words) > word_count:
        return ' '.join(words[:word_count]) + '...'
    return text