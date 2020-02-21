# import pandas as pd
import sqlite3


connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

# df = pd.read_csv('buddymove_holidayiq.csv')

# df.rename({'User Id': 'User_id'}, axis=1, inplace=True)

# print(df.head())

# print(df.shape)


# df.to_sql(name = 'review', con = connection)

total_query = """
SELECT
count(User_id)
FROM
review
"""

total_result = cursor.execute(total_query).fetchall()

print('\n')
print('There are', total_result[0][0], 'rows.\n')


nature_query = """
SELECT
count(User_id)
FROM
review
WHERE
(Nature > 99) & (Shopping > 99)
"""

nature_result = cursor.execute(nature_query).fetchall()

print('There are', nature_result[0][0], ("users who made at least 100"
      " reviews in both the Nature and Shopping categories.\n"))

categories = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']

for name in categories:
    average_query = """
    SELECT
    AVG({name})
    FROM
    review;
    """
    average_result = cursor.execute(average_query.format(name=name)).fetchall()
    print("The average number of reviews in the", name, "category is ",
          average_result[0][0], '\n')
