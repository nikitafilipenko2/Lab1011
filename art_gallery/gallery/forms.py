from django import forms
from .models import Artist, Museum, Painting

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'surname', 'birth_date']

class MuseumForm(forms.ModelForm):
    class Meta:
        model = Museum
        fields = ['name', 'city', 'country']

class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['name', 'creating_year', 'artist', 'museum']
