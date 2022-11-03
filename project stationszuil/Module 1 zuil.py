import datetime
import json
import random
import moderatie

datum_en_tijd = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

bericht = input('U kunt hier uw review achterlaten over het stationszuil met maximaal 140 karakters: ')
if len(bericht) >= 140:
    print('u mag maximaal 140 karakters invoeren')
    exit(bericht)


naam = input('Voer hier u naam als u niks invoert telt dit als een anonieme review: ')
if naam == '':
    naam = 'Anoniem'


station = random.choice(['Station Utrecht', 'Station Hilversum',
                         'Station Amsterdam',
                         'Station Amstelveen', 'Station Bunnik'])
print(station)
print(datum_en_tijd)

berichtinjson = {
    'naam': naam,
    'bericht': bericht,
    'station': station,
    'datatime.datatime.now()': str(datum_en_tijd)

}

with open('Stationszuil.json', 'r') as file:
    data = json.load(file)
    data.append(berichtinjson)

with open('Stationszuil.json', 'w') as file:
    json.dump(data, file, indent=True)

scheldwoorden = ['kut', 'kanker', 'lijer', 'poep', 'tering', 'hoer', 'slet', 'hoerezoon', 'aardappelhoer']

for scheldwoord in scheldwoorden:
    if scheldwoord in bericht:
        print('Dit bericht bevat geen correcte woorden hierdoor zal u recensie niet beoordeeld worden.')
        break
else:
    print('bedankt voor u recensie wij zullen hier naar kijken.')
