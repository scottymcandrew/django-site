from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    # title, link, and description attributes correspond to the <title>,<link>,<description> RSS elements
    title = 'My Blog'
    link = '/blog/'
    description = 'New posts of my blog'

    def items(self):
        return Post.published.all()[:5]

    # item_title() and item_description() methods receive each object returned by items(),
    # and return the title and description for each item
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
