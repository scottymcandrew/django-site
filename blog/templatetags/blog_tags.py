from django import template
from django.db.models import Count
from ..models import Post

# Each template tags module needs to contain a variable called register to be a valid tag library
register = template.Library()


# Django will use the function's name as the tag name.
# If you want to register it using a different name, you can do it by specifying a name attribute,
# such as @register.simple_tag(name='my_tag').
@register.simple_tag
def total_posts():
    return Post.published.count()


@register.simple_tag
def get_most_commented_posts(count=5):
    # annotate will aggregate the total number of comments for each post
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


# Using an inclusion tag, you can render a template with context variables returned by your template tag
@register.inclusion_tag('blog/post/latest_posts.html')
# count parameter optional and default set to 5
# The function returns a dictionary of variables instead of a simple value
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
