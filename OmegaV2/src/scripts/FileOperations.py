import datetime
import os
import traceback
import xml.etree.cElementTree as ET


def save_error(exc_type: type, exc_value, exc_tb: traceback):
    """
    Method that saves exception info into log file
    :param exc_type:
    :param exc_value:
    :param exc_tb:
    :return:
    """
    error_time = datetime.datetime.today().__str__()
    traceback_str = ''
    for trb in traceback.format_tb(exc_tb):
        traceback_str += trb
    log_path = './logs/error.log'
    print('siu')
    if not os.path.exists(log_path):
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        root = ET.Element("Error_log")
        tree = ET.ElementTree(root)
    else:
        tree = ET.parse(log_path)
    exc = ET.SubElement(tree.getroot(), "Exception")
    ET.SubElement(exc, 'Type').text = exc_type.__name__
    ET.SubElement(exc, 'Value').text = exc_value.__str__()
    ET.SubElement(exc, 'Traceback').text = traceback_str
    ET.SubElement(exc, 'Time').text = error_time
    ET.indent(tree, space="\t", level=0)
    string = ET.tostring(tree.getroot())
    with open(log_path, 'wb') as f:
        f.write(string)
