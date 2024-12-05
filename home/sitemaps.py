from django.urls import reverse
from products.models import Product
from django.conf import settings
from django.contrib.sitemaps import Sitemap


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'products', 'profile', 'product_sample']

    def location(self, item):
        if item == 'product_sample':
            return reverse('product_detail', kwargs={'product_id': 1})
        return reverse(item)

    # This is needed to get the sitemap view to use the site domain in the settings file!
    def get_urls(self, site=None, **kwargs):
        urls = super().get_urls(site=site, **kwargs)
        for url in urls:
            url['location'] = f"{settings.SITE_DOMAIN}{url['location']}"
        return urls


class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Product.objects.all()

    def location(self, item):
        return reverse('product_detail', kwargs={'product_id': item.id})

    def get_urls(self, site=None, **kwargs):
        urls = super().get_urls(site=site, **kwargs)
        for url in urls:
            url['location'] = f"{settings.SITE_DOMAIN}{url['location']}"
        return urls