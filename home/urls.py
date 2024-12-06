from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap, ProductSitemap


sitemaps = {
    'static': StaticViewSitemap,
    'product': ProductSitemap,
}

urlpatterns = [
    path('', views.index, name='home'),
    path('send-test-email/', views.send_test_email, name='send_test_email'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
