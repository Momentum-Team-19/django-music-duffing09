"""
URL configuration for config project.

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

# import various modules and functions needed for URLs and views. admin used for django admin interface, path used to define url patterns. views refers to views you've defined in django app
from django.contrib import admin
from django.urls import path, include
from django_music import views
from django.conf.urls.static import static
from django.conf import settings


# defining url patterns for application. each 'path' function call defines a URL pattern with its corresponding view function. first pattern links to django admin interface.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.album_list, name="album_list"),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/new', views.album_new, name='album_new'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('album/<pk>/remove/', views.album_remove, name='album_remove'),
    path('accounts/', include('registration.backends.simple.urls')),
]

# checks whether application is in debug mode. if it is it adds url pattern for servnc static files.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# this cod sets up URL patterns for your django application. When a user visits a specific URL, the corresponding view function from your views.py file is called to generate the appropriate HTML content. The urlpatterns list maps URLs to views, enabling navigation within my application. The 'if settings.DEBUG' block ensures that static files are served during development.