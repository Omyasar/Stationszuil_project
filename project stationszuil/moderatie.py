import datetime
import json
import psycopg2



with open('stationszuil.json', 'r') as file:
     data = json.load(file)


def datum_tijd():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def moderatornaam():
    return input('Wat is je moderator naam?: ')


def watisjemail():
    return input('voer hier je werkmail in: ')


def goedkeuring():
    bericht = input('is het bericht goedgekeurd? ja/nee ')
    if bericht == 'ja':
        return 'bericht is goedgekeurd'
    if bericht == 'nee':
        return 'bericht is afgekeurd'
    else:
        print('verkeerde input')

data_modded = []
for bericht in data:
    print(bericht)
    if goedkeuring() == 'bericht is goedgekeurd':
        bericht['naam_mod'] = moderatornaam()
        bericht['mail_mod'] = watisjemail()
        bericht['datum_mod'] = datum_tijd()
        data_modded.append(bericht)


with open('stationszuil_modded.json', 'w') as bestand:
    json.dump(data_modded, bestand, indent=True)

def databasevoeger(berichtinjson):
    conn = psycopg2.connect(
        host='localhost',
        dbname='project_stationszuil',
        user='postgres',
        password='farmainterim',
        port=5433)
    cursor = conn.cursor()
    bericht = f"""INSERT INTO bericht (naam, bericht, tijd, datum, station, moderator_nummer) 
                    VALUES (%s,%s,%s,%s,%s,%s);"""
    data = (berichtinjson['bericht']['naam'],berichtinjson['bericht']['bericht'],
            berichtinjson['bericht']['tijd'],berichtinjson['bericht']['datum'],
            berichtinjson['bericht']['station'])
    cursor.execute(bericht,data)
    conn.commit()
    conn.close()
















