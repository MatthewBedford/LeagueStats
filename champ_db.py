import sqlite3
import json

connection = sqlite3.connect('champ.db')


with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Loop through input from API that has data of champions and their icons and use that to store into local database.
with open('/home/matthew/environments/static/databaseInfo/champion.json') as f:
  champJSON = json.load(f)

for champion in champJSON['data']:

            inputChampID = champJSON['data'][champion]['key']
            inputChampName = champJSON['data'][champion]['name']
            inputChampIconText =  champJSON['data'][champion]['image']['full']
            
            cur.execute("INSERT INTO champions (champID, champName, icon) VALUES (?, ?, ?)",
                        (inputChampID, inputChampName, inputChampIconText)
                        )


connection.commit()
connection.close()