from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['index', 'product_search', 'about', 'contact', 'product_detail', 'checkout']  # Add the names of your views here

    def location(self, item):
        return reverse(item)