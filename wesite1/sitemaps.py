from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["wesite1:index", "wesite1:about", "wesite1:contact"]

    def location(self, item):
        return reverse(item)