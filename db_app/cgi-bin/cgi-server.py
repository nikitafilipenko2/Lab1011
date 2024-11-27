

import cgi
import sqlite3
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=utf-8\n")
print()

html_template = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>База данных: Картинная галлерея</title>

    <h1>Добавление новой художника</h1>
    <form method="post" action="">
        <label for="artist_id">ID:</label>
        <input type="number" id="artist_id" name="artist_id" required><br><br>
        
        <label for="name">Имя художника:</label>
        <input type="text" id="artist_name" name="artist_name" required><br><br>

        <label for="artist_surname">Фамилия художника:</label>
        <input type="text" id="artist_surname" name="artist_surname" required><br><br>

        <label for="birth_date">Дата рождения:</label>
        <input type="text" id="birth_date" name="birth_date" required><br><br>

        <input type="submit" value="Добавить">
    </form>
    <h2>Список всех художников</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Имя</th>
            <th>Фамилия</th>
            <th>Дата рождения</th>
        </tr>
        {artists_rows}
    </table>

    <h2>Добавить музей</h2>
    <form method="post" action="">
        <label for="museum_id">ID музея:</label>
        <input type="number" id="museum_id" name="museum_id" required><br><br>
        
        <label for="museum_name">Название музея:</label>
        <input type="text" id="museum_name" name="museum_name" required><br><br>
        
        <label for="museum_city">Город музея:</label>
        <input type="text" id="museum_city" name="museum_city" required><br><br>
        
        <label for="museum_country">Страна музея:</label>
        <input type="text" id="museum_country" name="museum_country" required><br><br>

        

        <input type="submit" value="Добавить музея">
    </form>
    <h2>Список музеев</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Название музея</th>
            <th>Город музея</th>
        </tr>
        {museums_rows}
    </table>

    <h2>Добавить картину</h2>
    <form method="post" action="">
    
        <label for="painting_id">ID картины:</label>
        <input type="number" id="painting_id" name="painting_id" required><br><br>
        
        <label for="painting_name">Название картины:</label>
        <input type="text" id="painting_name" name="painting_name" required><br><br>

        <label for="creating_year">Год создания картины:</label>
        <input type="text" id="creating_year" name="creating_year" required><br><br>
        
        <label for="painting_artist_id">ID художника:</label>
        <input type="number" id="painting_artist_id" name="painting_artist_id" required><br><br>
        
        <label for="painting_museum_id">ID музея:</label>
        <input type="number" id="painting_museum_id" name="painting_museum_id" required><br><br>

        <input type="submit" value="Добавить картину">
    </form>
    <h2>Список картин</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Название картины</th>
            <th>Год создания картины</th>
            <th>Художник</th>
            <th>Музей</th>
        </tr>
        {paintings_rows}
    </table>
</head>
</html>
"""


db_path = 'art_gallery.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


form = cgi.FieldStorage()


id=form.getvalue("artist_id")
name = form.getvalue("artist_name")
surname = form.getvalue("artist_surname")
birth_date = form.getvalue("birth_date")

if id and name and surname and birth_date:
    cursor.execute("INSERT INTO Artists (id,name, surname, birth_date) VALUES (?,?, ?, ?)",
                   (id,name, surname, birth_date))
    conn.commit()


museum_id = form.getvalue("museum_id")
museum_name = form.getvalue("museum_name")
museum_city=form.getvalue("museum_city")
museum_country=form.getvalue("museum_country")


if museum_id and museum_name and museum_city and museum_country:
    cursor.execute("INSERT INTO Museums (id,name, city,country) VALUES (?, ?,?,?)",
                   (int(museum_id),museum_name,museum_city,museum_country))
    conn.commit()

painting_id=form.getvalue("painting_id")
painting_name = form.getvalue("painting_name")
creating_year = form.getvalue("creating_year")
painting_artist_id=form.getvalue("painting_artist_id")
painting_museum_id=form.getvalue("painting_museum_id")

if painting_id and painting_name and creating_year and painting_artist_id and painting_museum_id:
    cursor.execute("INSERT INTO Paintings (id,name, creating_year, artist_id,museum_id) VALUES (?, ?, ?,?,?)",
                   (int(painting_id), painting_name, creating_year,int(painting_artist_id),int(painting_museum_id)))
    conn.commit()


cursor.execute("SELECT * FROM Artists")
artists_rows = cursor.fetchall()


cursor.execute("SELECT * FROM Museums")
museums_rows = cursor.fetchall()


cursor.execute("SELECT Paintings.id,Paintings.name, Paintings.creating_year,Artists.surname, Museums.name FROM Paintings inner join Artists on Paintings.artist_id=Artists.id inner join Museums on Paintings.museum_id=Museums.id")
paintings_rows = cursor.fetchall()

artists_html = ""
for row in artists_rows:
    artists_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
    </tr>
    """

museums_html = ""
for row in museums_rows:
    museums_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
    </tr>
    """

paintings_html = ""
for row in paintings_rows:
    paintings_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
        <td>{row[4]}</td>
    </tr>
    """


conn.close()


print(html_template.format(artists_rows=artists_html, museums_rows=museums_html,paintings_rows=paintings_html))
#python -m http.server --cgi 8000