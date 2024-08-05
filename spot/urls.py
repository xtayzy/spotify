from django.urls import path
from django.views.generic import TemplateView

from spot import views

urlpatterns = [
    path('', views.CategoryView.as_view(), name='index'),
    path('error', TemplateView.as_view(template_name='spot/error.html'), name='error'),
    path('genre/<int:pk>', views.GenreDetail.as_view(), name='genre'),
    path('music/<int:pk>', views.MusicDetail.as_view(), name='music'),
    path('history/', views.HistoryView.as_view(), name='history'),
    path('uploadmusic/', views.UploadMusicView.as_view(), name='upload'),
    path('playlists/', views.PlayListView.as_view(), name='playlist'),
    path('playlists/<int:pk>', views.PlayListDetailView.as_view(), name='playlist_detail'),
    path('playlist/<int:pk>/delete', views.PlaylistDeleteView.as_view(), name='playlist_delete'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('album/<int:pk>', views.AlbumDetail.as_view(), name='album')
]
