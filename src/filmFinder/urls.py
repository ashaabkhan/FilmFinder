"""filmFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from schema_graph.views import Schema

from .views import home_page, results_page, top_movies_page, movie_page
from accounts.views import login_page, register_page, account_page, register_genres_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="index"),
    url(r'^login/$', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('register_genres/', register_genres_page, name='register_genres'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('results/', results_page, name="result"),
    path('topmovies/', top_movies_page, name="topmovies"),
    path('account/', account_page, name="account"),
    url(r'^movie/(?P<movie_id>\d+)/$', movie_page, name="movie"),
    url(r"^schema/$", Schema.as_view()),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

