import pandas as pd
import sqlite3
con = sqlite3.connect("t2")

df = pd.read_sql(f'''
                        SELECT traveler_name, count(*) 
                        FROM traveler
                        JOIN place_traveler USING (traveler_id)
                        GROUP BY traveler_name 
                        ORDER BY traveler_name ASC;
                        ''', con)
print(df, '\n', '--------------------------------------------')
