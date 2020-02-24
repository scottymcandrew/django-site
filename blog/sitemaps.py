from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    # Returns the QuerySet of objects to include in this sitemap.
    # By default, Django calls the get_absolute_url() method on each object to retrieve its URL
    def items(self):
        return Post.published.all()

    # Receives each object returned by items() and returns the last time the object was modified.
    def lastmod(self, obj):
        return obj.updated
