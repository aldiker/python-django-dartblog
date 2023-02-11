from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('blog/claud_tags_tpl.html')
def get_claud_tags(cnt=0):
    if cnt == 0:
        tags = Tag.objects.all()
    else:
        tags = Tag.objects.all()[:cnt]
    return {'tags': tags}


@register.inclusion_tag('blog/search_post_tpl.html')
def search_post():
    return {}

