import pandas as pd
import sqlite3

DB_FILEPATH = 'Chinook_Sqlite.sqlite'

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

average_query = """
SELECT
    CustomerId,
    AVG(Total) as av
FROM Invoice
GROUP BY CustomerID
LIMIT 5
"""

result2 = cursor.execute(average_query).fetchall()
# print("RESULT 2", result2)

for row in result2:
    print('Customer #', row['CustomerId'], 'had average total', row['av'])
    print("-----")

notus_query = """
SELECT
    *
FROM 
    Customer
WHERE
    Country <> 'USA'
LIMIT 5
"""

result_notus = cursor.execute(notus_query).fetchall()
# print("RESULT 2", result2)
df = pd.DataFrame(columns = result_notus[0].keys())

for row in result_notus:
    df = df.append(dict(row), ignore_index = True)
    # print("-----")

print(df)

sabbath_query = """
SELECT
    Title, Track.Name
FROM
    Album
JOIN Artist
    ON
    Artist.ArtistId = Album.ArtistId
JOIN Track
    ON
    Album.AlbumId = Track.AlbumId
WHERE
    Artist.Name = 'Black Sabbath';
"""

# result_sabbath = cursor.execute(sabbath_query).fetchall()
df = pd.read_sql_query(sabbath_query, connection)
# for row in result_sabbath:
#     print(tuple(row))
print(df)