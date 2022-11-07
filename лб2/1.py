import sqlite3

con = sqlite3.connect("t2")
cursor = con.cursor()
cursor.executescript('''
                    CREATE TABLE IF NOT EXISTS city(
                        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_name VARCHAR(30)
                    );

                    INSERT INTO city (city_name)
                    VALUES
                    ('Yekaterinburg'),
                    ('Yakutsk'),
                    ('Changsha'),
                    ('Hangzhou');

                    CREATE TABLE IF NOT EXISTS country(
                        country_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        country_name VARCHAR(30)
                    );

                    INSERT INTO country (country_name)
                    VALUES
                    ('China'),
                    ('Russia');

                    CREATE TABLE IF NOT EXISTS place(
                      place_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      country_id INT,
                      city_id INT,
                      street VARCHAR(80),
                      sights VARCHAR(80),
                      transport_id INT,
                      FOREIGN KEY (country_id)  REFERENCES country (country_id) ON DELETE CASCADE,
                      FOREIGN KEY (city_id)  REFERENCES city (city_id) ON DELETE CASCADE);
                      
                    INSERT INTO place(country_id, city_id, street, sights, transport_id)  VALUES
                    (1, 1, 'The Bund', 60000, 1),
                    (1, 2, 'Central Avenue', 10000, 2),
                    (1, 3, 'Du jiang yan', 30000, 1),
                    (1, 4, 'Wangfujing Street', 50000, 1),
                    (1, 5, 'Baita Mountain', 40000, 1),
                    (2, 6, 'Red Square', 80000, 3),
                    (2, 7, 'Oceanarium', 40000, 1),
                    (2, 8, 'Winter Palace', 80000, 1),
                    (1, 9, 'Fangchuan Scenic Area', 30000, 3),
                    (1, 10, 'Nanshan Temple', 80000, 1),
                    (1, 11, 'Fengdu Ghost Town', 40000, 1);
                    
                    ''')


