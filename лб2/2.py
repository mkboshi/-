import sqlite3

con = sqlite3.connect("t2")
cursor = con.cursor()

cursor.execute('''
                SELECT * 
                    FROM place_traveler 
                    WHERE ID IN (SELECT ID 
                              FROM place_traveler
                              WHERE place = 2);
                ''')
print(cursor.fetchall(), '\n')

cursor.execute('''
                UPDATE place
                     SET sights = sights * 0.50
                     WHERE traveler IN (SELECT traveler FROM place_traveler
                                   WHERE traveler >= 5 );
                                   ''')
print(cursor.fetchall(), '\n')
