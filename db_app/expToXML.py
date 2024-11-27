import sqlite3
from xml.dom.minidom import Document

conn = sqlite3.connect('сgi-bin/art_gallery.db')
cursor = conn.cursor()
print("Content-Type: text/html; charset=utf-8\n")
cursor.execute("SELECT * FROM Artists")
artists = cursor.fetchall()

cursor.execute("SELECT * FROM Museums")
museums = cursor.fetchall()

cursor.execute("SELECT * FROM Paintings")
paintings = cursor.fetchall()


doc = Document()


root = doc.createElement('dbData')
doc.appendChild(root)


for artist in artists:

    artist_element = doc.createElement('Artist')
    root.appendChild(artist_element)

    id_element = doc.createElement('id')
    id_element.appendChild(doc.createTextNode(str(artist[0])))
    artist_element.appendChild(id_element)

    name_element = doc.createElement('name')
    name_element.appendChild(doc.createTextNode(artist[1]))
    artist_element.appendChild(name_element)

    birth_year_element = doc.createElement('birth_year')
    birth_year_element.appendChild(doc.createTextNode(str(artist[2])))
    artist_element.appendChild(birth_year_element)

    country_element = doc.createElement('country')
    country_element.appendChild(doc.createTextNode(artist[3]))
    artist_element.appendChild(country_element)

for museum in museums:

    museum_element = doc.createElement('Museum')
    root.appendChild(museum_element)


    id_element = doc.createElement('id')
    id_element.appendChild(doc.createTextNode(str(museum[0])))
    museum_element.appendChild(id_element)

    name_element = doc.createElement('name')
    name_element.appendChild(doc.createTextNode(museum[1]))
    museum_element.appendChild(name_element)

    city_element = doc.createElement('city')
    city_element.appendChild(doc.createTextNode(str(museum[2])))
    museum_element.appendChild(city_element)

    country_element = doc.createElement('country')
    country_element.appendChild(doc.createTextNode(museum[3]))
    museum_element.appendChild(country_element)

for painting in paintings:

    painting_element = doc.createElement('Painting')
    root.appendChild(painting_element)


    id_element = doc.createElement('id')
    id_element.appendChild(doc.createTextNode(str(painting[0])))
    painting_element.appendChild(id_element)

    name_element = doc.createElement('name')
    name_element.appendChild(doc.createTextNode(painting[1]))
    painting_element.appendChild(name_element)

    creating_year_element = doc.createElement('creating_year')
    creating_year_element.appendChild(doc.createTextNode(str(painting[2])))
    painting_element.appendChild(creating_year_element)

    artist_id_element = doc.createElement('artist_id')
    artist_id_element.appendChild(doc.createTextNode(str(painting[3])))
    painting_element.appendChild(artist_id_element)

    museum_id_element = doc.createElement('museum_id')
    museum_id_element.appendChild(doc.createTextNode(str(painting[4])))
    painting_element.appendChild(museum_id_element)


with open("dbData.xml", "w", encoding="utf-8") as xml_file:
    xml_file.write(doc.toprettyxml(indent="  "))


conn.close()