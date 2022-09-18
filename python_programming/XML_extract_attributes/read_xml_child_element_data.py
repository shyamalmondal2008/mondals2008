from xml.dom import minidom

file = minidom.parse("model_xml.xml")
models = file.getElementsByTagName('model')

for elements in models:
    print(elements.attributes['name'].value, 'value is', elements.firstChild.data)
