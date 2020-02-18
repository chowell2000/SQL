
import sqlite3

DB_FILEPATH = 'rpg_db.sqlite3'

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
# print("Connection", connection)

cursor = connection.cursor()
# print("Cursor", cursor)

total_character_query = """
    SELECT
    count(character_id)
    FROM
    charactercreator_character
    """

result_total_character = cursor.execute(total_character_query).fetchall()

print('\nThe total number of characters is', result_total_character[0][0])

classes = ['cleric', 'fighter', 'mage', 'thief']

for classes in classes:
    # print(classes)
    class_db = 'charactercreator_' + classes
    classeses = classes + 's'
    class_query = """
                    SELECT
                    count(character_ptr_id)
                    FROM
        """ + class_db
    class_total_result = cursor.execute(class_query).fetchall()
    print(" \nThe total number of",  classeses, 'is: ',
          class_total_result[0][0])

necro_query = """
        SELECT
        count(mage_ptr_id)
        FROM
        charactercreator_necromancer
        """
necro_total_result = cursor.execute(necro_query).fetchall()
print(" \nThe total number of necromancers is: ",
      necro_total_result[0][0])
print("""
 The necromancers are also included as mages,
 so they are counted twice in this list
 """)

item_total_query = """
        SELECT
        count(item_id)
        FROM
        armory_item
        """
item_total_result = cursor.execute(item_total_query).fetchall()
print(" \nThe total number of items is: ",
      item_total_result[0][0])

weapon_query = """
        SELECT
        count(item_ptr_id)
        FROM
        armory_weapon
        """
weapon_result = cursor.execute(weapon_query).fetchall()
print(" \nThe total number of weapons is: ",
      weapon_result[0][0])
print(" \nThe total number of items that are not weapons is: ",
      item_total_result[0][0] - weapon_result[0][0], '\n')


character_item_query = """
SELECT
    character_id,
    count(distinct item_id) as Item_Count
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""
character_item_result = cursor.execute(character_item_query).fetchall()
for row in character_item_result:
    print('Character number:', row['character_id'],
          'has', row['Item_Count'], 'items')

print('next test')
