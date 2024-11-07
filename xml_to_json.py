"""
Example of how to convert from XML to JSON.
"""

import xml.etree.ElementTree as ET
import json


def build_students_list(root) -> list:
    """
    Build a list of student dictionaries from an XML root element.

    Unlike when we convert json to xml, this method needs knowledge of the xml structure
    to do the conversion correctly.
    
    :param root: The root element of the XML data.
    :return: A list of student dictionaries.
    """
    students_list = []
    for student in root.findall('student'):
        student_data = {
            'fullName': {
                'title': student.find('fullName').get('title'),
                'firstName': student.find('fullName/firstName').text,
                'surname': student.find('fullName/surname').text,
            },
            'age': int(student.find('age').text),
            'city': student.find('city').text
        }

        # Handle 'other' names if present
        other_element = student.find('fullName/other')
        if other_element is not None:
            other_names = [name.text for name in other_element.findall('name')]
            student_data['fullName']['other'] = {
                'num': int(other_element.get('num')),
                'names': other_names
            }

        students_list.append(student_data)
        return students_list


def load_xml(file_path: str) -> ET.Element:
    """
    Load XML data from a file.
    
    :param file_path: The path to the XML file.
    :return: The root element of the XML data.
    """
    with open(file_path, 'r', encoding='UTF-8') as file:
        xml_data = file.read()
    return ET.fromstring(xml_data)


def write_json(file_path: str, data: dict):
    """
    Write JSON data to a file.
    
    :param file_path: The path to the JSON file.
    :param data: The data to write.
    """
    with open(file_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    xml_root = load_xml('People.xml')
    students = build_students_list(xml_root)
    write_json('output.json', {'students': students})
    print('JSON file saved successfully.')
