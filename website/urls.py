from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from webapp1.sitemaps import StaticViewSitemap
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'webapp1.views.handler404'

sitemaps = {
    'static': StaticViewSitemap,
    # Add more sitemaps if needed
}


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

admin.site.site_header = "ElectroShop"
admin.site.site_title = "ElectroShop Admin Panel"
admin.site.index_title = "ElectroShop Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp1.urls')),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
# Serve static files during development when DEBUG is False
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

