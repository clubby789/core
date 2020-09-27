"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import os

from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('announcements/', include('announcements.urls')),
    path('auth/', include('authentication.urls')),
    path('challenges/', include('challenge.urls')),
    path('challengeserver/', include('challengeserver.urls')),
    path('config/', include('config.urls')),
    path('leaderboard/', include('leaderboard.urls')),
    path('member/', include('member.urls')),
    path('stats/', include('stats.urls')),
    path('team/', include('team.urls')),
    path('pages/', include('pages.urls')),
]

if "silk" in settings.INSTALLED_APPS:
    urlpatterns += [path('silk/', include('silk.urls'))]

if not os.getenv("USE_AWS"):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
