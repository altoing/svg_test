#! /usr/bin/env python3
# Парсит svg файл сгенерированный из visio. Добовляет класс к синим эементам из дескрипшена
import xml.etree.ElementTree as ET
tree = ET.parse('in.svg')
root = tree.getroot()

ET.register_namespace('', "http://www.w3.org/2000/svg")
ET.register_namespace('ev', "http://www.w3.org/2001/xml-events")
ET.register_namespace('xlink', "http://www.w3.org/1999/xlink")
ET.register_namespace('v', "http://schemas.microsoft.com/visio/2003/SVGExtensions/")

fg = root[4][1]
list = [x for x in fg]
for x in list:
	for xx in x.findall('.//{http://www.w3.org/2000/svg}desc'):
		description = xx.text
		description = description.replace(" ", "_")
		description = description.replace(".", "")
	for dd in x.findall('.//{http://www.w3.org/2000/svg}g[@fill="#046897"]'):
		dd.set('class', description) 
	for dz in x.findall('.//{http://www.w3.org/2000/svg}g[@fill="#036c9b"]'):
		dd.set('class', description) 	

tree.write('out.svg')
