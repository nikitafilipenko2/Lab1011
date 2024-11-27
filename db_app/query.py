import sqlite3

connection = sqlite3.connect('сgi-bin/art_gallery.db')
cursor = connection.cursor()
print("Content-Type: text/html; charset=utf-8\n")
artist_name = 'Vincent'
cursor.execute('''
SELECT Paintings.name, Paintings.creating_year
FROM Paintings 
JOIN Artists ON Paintings.artist_id = Artists.id 
WHERE Artists.name = ?
''', (artist_name,))
print(cursor.fetchall())

museum_name='Sistina capella'
cursor.execute('''
SELECT Paintings.name, Paintings.creating_year
FROM Paintings 
join Museums on Paintings.museum_id=Museums.id
where Museums.name=?
''',(museum_name,))
print(cursor.fetchall())


city = 'New York'
cursor.execute('''
SELECT id,name
FROM Museums 
WHERE city = ?
''', (city,))
print(cursor.fetchall())