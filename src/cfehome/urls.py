"""muypicky URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from restaurants.views import (
    score_listview,
    ScoreListView,
    ScoreDetailView,
    score_createview

)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^restaurants/$', ScoreListView.as_view()),
    #url(r'^restaurants/(?P<slug>\w+)/$', ScoreListView.as_view()),
    url(r'^restaurants/create/$', score_createview),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', ScoreDetailView.as_view()),
    
    #url(r'^restaurants/asian/$', AsianFusionRestaurantListView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
]