from django import forms

from spot.models import Music, PlayList


class AddMusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name', 'image', 'file', 'album', 'genres']


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = PlayList
        fields = ['name', 'is_public']