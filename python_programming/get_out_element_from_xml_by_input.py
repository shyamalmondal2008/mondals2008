import xml.etree.ElementTree as ET


def timestamps_by_description(country_name):
    global name
    mystring = """<?xml version="1.0"?>
    <data>
        <country name="Liechtenstein">
            <rank>1</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor name="Austria" direction="E"/>
            <neighbor name="Switzerland" direction="W"/>
        </country>
        <country name="Panama">
            <rank>68</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor name="Costa Rica" direction="W"/>
            <neighbor name="Colombia" direction="E"/>
        </country>
        <country name="Singapore">
            <rank>4</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor name="Malaysia" direction="N"/>
        </country>

    </data>"""

    root = ET.fromstring(mystring)
    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')
        if name == country_name:
            print(name, rank)


timestamps_by_description("Panama")


