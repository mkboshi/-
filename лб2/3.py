import sqlite3
import pandas as pd

con = sqlite3.connect("t2")
df = pd.read_sql('''
                SELECT country_name AS Страна, city_name AS Город, street AS Улица,  sights AS Цена
                FROM place
                JOIN city USING (city_id)
                JOIN country USING (country_id)
                WHERE sights > 30000;
                ''', con)
print(df, '\n', '-----------------------------------')
print(df['Улица'], '\n', '-----------------------------------')
print(df.loc[2], '\n', '-----------------------------------')
print(df.shape[0], ' ', df.shape[1], '\n', '-----------------------------------')
print(df.dtypes.index, '\n', '-----------------------------------')