from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from spot.forms import AddMusicForm, PlaylistForm
from spot.models import Genre, Music, History, PlayList, Album


# Create your views here.

@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class CategoryView(ListView):
    template_name = 'spot/index.html'
    model = Genre
    context_object_name = 'genres'


@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class GenreDetail(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'spot/genre_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = context.get('genre')
        print(genre.musics.all())
        context['musics'] = genre.musics.all()
        return context


@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class MusicDetail(DetailView):
    template_name = 'spot/music.html'
    model = Music
    context_object_name = 'music'

    def get(self, request, *args, **kwargs):
        History.objects.create(
            music=Music.objects.get(pk=self.kwargs['pk']),
            user=self.request.user
        )
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        music = Music.objects.get(pk=kwargs['pk'])
        playlist = PlayList.objects.get(pk=self.request.POST['playlist'])
        playlist.musics.add(music)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        music = context.get('music')
        genres = music.genres.all()
        context['genres'] = genres
        context['genres_str'] = ', '.join(map(lambda genre: genre.name, genres))

        context['playlists'] = self.request.user.playlists.all()
        return context


@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class HistoryView(ListView):
    template_name = 'spot/history.html'
    model = History
    context_object_name = 'histories'
    paginate_by = 15

    def get_queryset(self):
        return History.objects.filter(user=self.request.user).order_by('-listened_at')


class UploadMusicView(CreateView):
    template_name = 'spot/upload_music.html'
    model = Music
    form_class = AddMusicForm

    def form_valid(self, form):
        music = form.save(commit=False)
        music.author = self.request.user
        music.save()
        form.save_m2m()

        return redirect('index')


@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class PlayListView(ListView):
    model = PlayList
    context_object_name = 'playlists'
    template_name = 'spot/playlist.html'

    def get_queryset(self):
        return PlayList.objects.filter(author=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        new_playlists = []
        for playlist in ctx['playlists']:
            musics = playlist.musics.all()
            new_playlist = {
                'id': playlist.id,
                'name': playlist.name,
                'musics': musics,
                'created_at': playlist.created_at,
                'image': musics[0].image.url if len(musics) > 0 else '/media/default.jpg'
            }
            new_playlists.append(new_playlist)
        ctx['new_playlists'] = new_playlists
        ctx['form'] = PlaylistForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = PlaylistForm(self.request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.author = self.request.user
            playlist.save()
        return super().get(*args, **kwargs)


@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class PlayListDetailView(DetailView):
    template_name = 'spot/playlist_detail.html'
    model = PlayList
    context_object_name = 'playlist'

    def get(self, request, *args, **kwargs):
        playlist = PlayList.objects.get(pk=self.kwargs['pk'])
        if request.user.id != playlist.author.id:
            if not playlist.is_public:
                return redirect('error')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        playlist = PlayList.objects.get(pk=kwargs['pk'])
        music = Music.objects.get(pk=self.request.POST['music'])
        playlist.musics.remove(music)

        return super().get(request, *args, **kwargs)


@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class PlaylistDeleteView(DeleteView):
    template_name = 'spot/delete_confirm.html'
    model = PlayList
    context_object_name = 'playlist'

    def post(self, request, *args, **kwargs):
        playlist = PlayList.objects.get(pk=self.kwargs['pk'])
        if playlist.author.id != self.request.user.id:
            return redirect('error')
        playlist.delete()
        return redirect('playlist')


class AlbumListView(ListView):
    template_name = 'spot/albums.html'
    model = Album
    context_object_name = 'albums'


@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class AlbumDetail(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'spot/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = context.get('album')
        context['musics'] = album.musics.all()
        return context




