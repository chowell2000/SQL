import os
import sqlite3

DB_FILEPATH = 'chinook.db'

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
print("Connection", connection)

cursor = connection.cursor()
print("Cursor", cursor)

query = """
SELECT
    country,
    count(distinct CustomerId) as CustomerCount
FROM customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5
"""

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    # print(type(row))
    # print(row)
    print(row['Country'])
    print(row["CustomerCount"])
    print("-----")
