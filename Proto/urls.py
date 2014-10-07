from django.conf.urls import patterns, include, url
from django.contrib import admin
from project import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^project/players_text/$', views.players_text, name="players_text"),
    url(r'^project/players/$', views.players, name="players"),
    url(r'^project/matchs/$', views.matchs, name="matchs"),
    url(r'^project/api/players', views.players_json, name="players_json"),
    url(r'^project/players_details/(?P<player_id>\d+)', views.player_details, name="player_details"),
)
