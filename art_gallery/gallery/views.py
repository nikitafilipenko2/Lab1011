from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Museum, Painting
from .forms import ArtistForm, MuseumForm, PaintingForm

# Удаление художника
def artist_delete(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return redirect('artist_list')

# Удаление музея
def museum_delete(request, pk):
    museum = get_object_or_404(Museum, pk=pk)
    museum.delete()
    return redirect('museum_list')

# Удаление картины
def painting_delete(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    painting.delete()
    return redirect('painting_list')
def artist_add(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_list')  # Перенаправление на страницу списка художников
    else:
        form = ArtistForm()
    return render(request, 'gallery/artist_form.html', {'form': form})

# Форма добавления музея
def museum_add(request):
    if request.method == 'POST':
        form = MuseumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('museum_list')  # Перенаправление на страницу списка музеев
    else:
        form = MuseumForm()
    return render(request, 'gallery/museum_form.html', {'form': form})

# Форма добавления картины
def painting_add(request):
    if request.method == 'POST':
        form = PaintingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painting_list')  # Перенаправление на страницу списка картин
    else:
        form = PaintingForm()
    return render(request, 'gallery/painting_form.html', {'form': form})
# Список музеев
def museum_list(request):
    museums = Museum.objects.all()
    return render(request, 'gallery/museum_list.html', {'museums': museums})

# Детальная информация о музее
def museum_detail(request, pk):
    museum = get_object_or_404(Museum, pk=pk)
    return render(request, 'gallery/museum_detail.html', {'museum': museum})

# Добавление нового музея


# Редактирование музея
def museum_edit(request, pk):
    museum = get_object_or_404(Museum, pk=pk)
    if request.method == 'POST':
        form = MuseumForm(request.POST, instance=museum)
        if form.is_valid():
            form.save()
            return redirect('museum_list')  # Перенаправление на страницу списка музеев
    else:
        form = MuseumForm(instance=museum)
    return render(request, 'gallery/museum_form.html', {'form': form})


# Главная страница
def index(request):
    return render(request, 'gallery/index.html')

# Список художников
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'gallery/artist_list.html', {'artists': artists})


# Список картин
def painting_list(request):
    paintings = Painting.objects.all()
    return render(request, 'gallery/painting_list.html', {'paintings': paintings})

# Детальная информация о художнике
def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'gallery/artist_detail.html', {'artist': artist})

# Детальная информация о картине
def painting_detail(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    return render(request, 'gallery/painting_detail.html', {'painting': painting})

# Добавление нового художника


# Добавление новой картины


# Редактирование художника
def artist_edit(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_list')  # Перенаправление на страницу списка художников
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'gallery/artist_form.html', {'form': form})

# Редактирование картины
def painting_edit(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    if request.method == 'POST':
        form = PaintingForm(request.POST, instance=painting)
        if form.is_valid():
            form.save()
            return redirect('painting_list')  # Перенаправление на страницу списка картин
    else:
        form = PaintingForm(instance=painting)
    return render(request, 'gallery/painting_form.html', {'form': form})

# Удаление картины
def painting_delete(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    painting.delete()
    return redirect('painting_list')
