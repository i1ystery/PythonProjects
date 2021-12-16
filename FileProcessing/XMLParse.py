import xml.etree.ElementTree as ET


def person_search(xml_path):
    xml = ET.parse(xml_path)
    root = xml.getroot()
    for person in root.iter('{http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_datatypes/v_1.0.5}Osoba'):
        for info in person:
            print(info.text)
        print()


person_search('xmltoparse.xml')
