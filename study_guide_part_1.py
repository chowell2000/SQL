import sqlite3

connection = sqlite3.connect('study_1.sqlite3')
# connection.row_factory = sqlite3.Row
cursor = connection.cursor()

new_table = """
CREATE TABLE
    students
    (
    student  VARCHAR(40),
    studied  VARCHAR(20),
    grade  INT,
    age  INT,
    sex  VARCHAR(10)
    );
"""

new_data = """
INSERT  INTO
    students
    (student, studied, grade, age, sex)
VALUES
    ('Lion-O', 'True', 85, 24, 'Male'),
    ('Cheetara', 'True', 95, 22, 'Female'),
    ('Mumm-Ra', 'False', 65, 153, 'Male'),
    ('Snarf', 'False', 70, 15, 'Male'),
    ('Panthro', 'True', 80, 30, 'Male');
"""

cursor.execute(new_table)
cursor.execute(new_data)
connection.commit()

age_query = """
SELECT
    AVG(age)
FROM
    students;
"""

female_query = """
SELECT
    student
FROM
    students
WHERE
    sex = 'Female';
"""

studied_query = """
SELECT
    count(student)
FROM
    students
WHERE
    studied = 'True';
"""

alph_query = """
SELECT
    *
FROM
    students
ORDER BY
    student;
"""


avg_age = cursor.execute(age_query).fetchall()
print('average age', avg_age[0][0])

studied = cursor.execute(studied_query).fetchall()
print('Students who studied numbered', studied[0][0])

female = cursor.execute(female_query).fetchall()
print('Female student is', female[0][0])

alph = cursor.execute(alph_query).fetchall()
print(alph)


connection.close()
