import xml.etree.ElementTree as ET

def xml_to_file():
    tree = ET.parse("path_to_file.xml")

    root = tree.getroot()

    return root

def xml_to_string():
    xml_data = '''<?xml version="1.0"?>
    <saluti>
    <saluto>Hello World</saluto>
    </saluti>'''

    root = ET.fromstring(xml_data)

    return root

#root = xml_to_file()

root = xml_to_string()

for saluto in root.findall('saluto'):                           #cerca tutti gli elementi
    print(saluto.text)

saluto = root.find('saluto')                                #cerca il primo elemento
print(saluto.text)
print(saluto.attrib)                                         #stampa il dizionario

root.write("file.xml")                                      #salva tutto in un file


new_element = ET.Element('nuovo_tag')

new_element.text = "testo del nuovo elemento"

root.append(new_element)

#tree.write('file.xml')

tree = ET.ElementTree(root)


