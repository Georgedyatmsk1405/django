from django.contrib.sitemaps import Sitemap
from app_houses.models import House

class HouseSitemap(Sitemap):
    changefreq='weekly'
    priority =0.9
    def items(self):
        return House.objects.all()
    def lastmod(self, obj:House):
        return obj.published_at