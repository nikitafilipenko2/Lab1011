import sqlite3

connection = sqlite3.connect('art_gallery.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Artists (
id INTEGER PRIMARY KEY ,
name TEXT NOT NULL,
surname TEXT NOT NULL,
birth_date TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Museums (
id INTEGER PRIMARY KEY ,
name TEXT NOT NULL,
city TEXT NOT NULL,
country TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Paintings (
id INTEGER PRIMARY KEY ,
name TEXT NOT NULL,
creating_year TEXT,
artist_id INTEGER,
museum_id INTEGER,
FOREIGN KEY (artist_id)  REFERENCES Artists (id),
FOREIGN KEY (museum_id)  REFERENCES Museums (id)
)
''')

cursor.execute('''
INSERT INTO Artists VALUES (1,'Vincent','Van-Gog','03-30-1853')
''')
cursor.execute('''
INSERT INTO Artists VALUES (2,'Mikelanjelo','Buonarotti','03-06-1475')
''')
cursor.execute('''
INSERT INTO Artists VALUES (3,'Viktor','Vasnetcov','05-15-1848')
''')

cursor.execute('''
INSERT INTO Museums VALUES (1,'Tretyakovskaya gallery','Moscow','Russia')
''')
cursor.execute('''
INSERT INTO Museums VALUES (2,'Sistina capella','Vatikan','Italy')
''')
cursor.execute('''
INSERT INTO Museums VALUES (3,'Museum of modern art','New York','USA')
''')

cursor.execute('''
INSERT INTO Paintings VALUES (1,'Bogatyrs','04-23-1898',3,1)
''')
cursor.execute('''
INSERT INTO Paintings VALUES (2,'Creation of Adam','??-??-1511',2,2)
''')
cursor.execute('''
INSERT INTO Paintings VALUES (3,'Star night','06-06-1889',1,3)
''')

connection.commit()
connection.close()