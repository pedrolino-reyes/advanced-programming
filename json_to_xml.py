"""
Example of how to convert from JSON to XML.
"""

import json
import xml.etree.ElementTree as ET


def json_to_xml(json_obj: dict, root_name: str) -> ET.ElementTree:
    """
    Convert a JSON object to an XML ElementTree object.


    :param json_obj: The JSON object to convert.
    :param root_name: The name of the root element.
    :return: An ElementTree object.
    """
    root = ET.Element(root_name)

    def build_tree(elem, structure):
        if isinstance(structure, dict):
            for k, v in structure.items():
                child = ET.SubElement(elem, k)
                build_tree(child, v)
        elif isinstance(structure, list):
            for item in structure:
                child = ET.SubElement(elem, 'item')
                build_tree(child, item)
        else:
            elem.text = str(structure) if structure is not None else ''

    build_tree(root, json_obj)
    return ET.ElementTree(root)


def load_json(file_path: str) -> dict:
    """
    Load JSON data from a file.

    :param file_path: The path to the JSON file.
    :return: The JSON data as a dictionary.
    """
    with open(file_path, 'r', encoding='UTF-8') as file:
        return json.load(file)


def save_xml(xml_tree: ET.ElementTree, file_path: str):
    """
    Save an XML ElementTree to a file.

    :param xml_tree: The ElementTree object to save.
    :param file_path: The path to save the XML file.
    """
    xml_tree.write(file_path, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    json_data = load_json('People.json')
    tree = json_to_xml(json_data, 'data')
    save_xml(tree, 'output.xml')
    print('XML file saved successfully.')
