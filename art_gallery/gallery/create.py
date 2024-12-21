from models import Artist, Museum, Painting

# Создание художников
artist1 = Artist.objects.create(name='Vincent', surname='Van Gogh', birth_date='1853-03-30')
artist2 = Artist.objects.create(name='Michelangelo', surname='Buonarroti', birth_date='1475-03-06')
artist3 = Artist.objects.create(name='Viktor', surname='Vasnetsov', birth_date='1848-05-15')

# Создание музеев
museum1 = Museum.objects.create(name='Tretyakov Gallery', city='Moscow', country='Russia')
museum2 = Museum.objects.create(name='Sistine Chapel', city='Vatican', country='Italy')
museum3 = Museum.objects.create(name='Museum of Modern Art', city='New York', country='USA')

# Создание картин
painting1 = Painting.objects.create(name='Bogatyrs', creating_year='1898', artist=artist3, museum=museum1)
painting2 = Painting.objects.create(name='Creation of Adam', creating_year='1511', artist=artist2, museum=museum2)
painting3 = Painting.objects.create(name='Starry Night', creating_year='1889', artist=artist1, museum=museum3)

print("Данные успешно добавлены!")
