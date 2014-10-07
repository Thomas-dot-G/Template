from django.conf.urls import patterns, include, url
from django.contrib import admin
from project import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^project/$', views.index, name="index"),
    url(r'^project/players/$', views.players, name="players"),
    url(r'^project/players2/$', views.players2, name="players2"),
    url(r'^project/matchs/$', views.matchs, name="matchs"),
    url(r'^project/api/players/$', views.playersJSON, name="playersJSON"),
    url(r'^project/playerDetails/(?P<player>\w+)/$', views.playerDetails, name="playerDetails"),
)
