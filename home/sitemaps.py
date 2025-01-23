from django.urls import reverse
from products.models import Product
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from urllib.parse import urlparse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'products', 'profile']

    def location(self, item):
        return reverse(item)

    # This rather involved rigmarole seems to be needed to get the sitemap view
    # to use the site domain in the settings file without concatenating
    # "https//example.com"! It's a workaround. There is almost certainly
    # a better way!
    def get_urls(self, site=None, **kwargs):
        urls = super().get_urls(site=site, **kwargs)
        for url in urls:
            parsed_url = urlparse(url['location'])
            if not parsed_url.netloc:
                url['location'] = f"{settings.SITE_DOMAIN}{url['location']}"
            else:
                url['location'] = f"{settings.SITE_DOMAIN}{parsed_url.path}"
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
            parsed_url = urlparse(url['location'])
            if not parsed_url.netloc:
                url['location'] = f"{settings.SITE_DOMAIN}{url['location']}"
            else:
                url['location'] = f"{settings.SITE_DOMAIN}{parsed_url.path}"
        return urls
