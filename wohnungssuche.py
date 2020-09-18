import requests
import json
from bs4 import BeautifulSoup

URL = 'https://www.vermietungen.stadt-zuerich.ch'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

for wohnung in soup.findAll('tr'):
    title_elem = None
    building_elem = None
    rentalgross_elem = None
    rentalgross_net_elem = None
    rooms_elem = None
    property_type_elem = None
    # etc
    for field in wohnung.findAll('td'):
        if field.attrs['class'] == ['title']:
            title_elem = field.text
            title_elem = title_elem.replace('\n', '')
        if field.attrs['class'] == ['building']:
            building_elem = field.text
            building_elem = building_elem.replace('\n', '')
        if field.attrs['class'] == ['rentalgross']:
            rentalgross_elem = field.text
            rentalgross_elem = rentalgross_elem.replace('\n', '')
            rentalgross_elem = rentalgross_elem.replace(' ', '')
        if field.attrs['class'] == ['rentalgross_net']:
            rentalgross_net_elem = field.text
            rentalgross_net_elem = rentalgross_net_elem.replace('\n', '')
            rentalgross_net_elem = rentalgross_net_elem.replace(' ', '')
        if field.attrs['class'] == ['rooms']:
            rooms_elem = field.text
            rooms_elem = rooms_elem.replace('\n', '')
            rooms_elem = rooms_elem.replace(' ', '')
        if field.attrs['class'] == ['property_type']:
            property_type_elem = field.text
            property_type_elem = property_type_elem.replace('\n', '')
            property_type_elem = property_type_elem.replace(' ', '')

    apartment = {
            'title': title_elem,
            'building': building_elem,
            'rentalgross': rentalgross_elem,
            'rentalgross_net': rentalgross_net_elem,
            'rooms': rooms_elem,
            'property_type': property_type_elem
    }

    with open('data.json') as localdb:
        testdata = json.load(localdb)
        testdataapartment = testdata['apartment']
        if apartment in testdataapartment:
            print("Apartment already exists in the local database")
        else:
            def write_json(data, filename='data.json'):
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f,ensure_ascii=False, indent=4)


            with open('data.json') as json_file:
                data = json.load(json_file)
                temp = data['apartment']
                temp.append(apartment)

            write_json(data)







