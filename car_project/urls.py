"""
URL configuration for car_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from main.views import LandingView, CustomerRequestFormView, redirect_main


handler404 = 'main.views.customhandler404'
handler500 = 'main.views.customhandler500'

urlpatterns = [
    path("uk/target-page/", LandingView.as_view(), name='target_page'),
    path("i18n/", include("django.conf.urls.i18n")),
    path("moderatory/", admin.site.urls),
    path("save_form/", CustomerRequestFormView.as_view()),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(template_name="sitemap.xml", content_type="text/plain"),
    ),
    path("uk/", redirect_main)
]

urlpatterns += i18n_patterns(
    path("", LandingView.as_view(), name='main'),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
