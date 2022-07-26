"""retropc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("store.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path("profile/", include("user_account.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="home/robots.txt", content_type="text/plain"
        ),
    ),  # add the robots.txt file
    path(
        "sitemap.xml",
        TemplateView.as_view(template_name="home/sitemap.xml", content_type="text/xml"),
    ),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "retropc.views.handler404"
