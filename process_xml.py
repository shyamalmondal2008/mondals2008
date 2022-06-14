import xml.etree.ElementTree as ET


def extract_country_rank(in_country):
    tree = ET.parse('country_data.xml')
    root = tree.getroot()

    for country1 in root.findall('country'):
        rank = country1.find('rank').text
        name = country1.get('name')
        if name == in_country:
            print(name, rank)


extract_country_rank('Singapore')
