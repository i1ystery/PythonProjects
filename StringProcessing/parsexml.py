import re
import xml.etree.ElementTree as ET

# import requests
#
# URL = "https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_rzp.cgi?ico=27074358"
#
# response = requests.get(URL)
# with open('xmltoparse.xml', 'wb') as file:
#     file.write(response.content)


def person_search(xml):
    xml_str = ET.tostring(xml.getroot(), encoding='unicode')
    print(xml_str)
    fo = re.findall(r'<ns2:J>(.*)</ns2:J>\n<ns2:P>(.*)</ns2:P>\n<ns2:DN>(.*)</ns2:DN>', xml_str)
    return fo


x = person_search(ET.parse('xmltoparse.xml'))
fo = x
for x in fo:
    print(x[0] + ' ' + x[1] + ' ' + x[2])