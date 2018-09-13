import sys
from xml.dom import minidom
import re

if len(sys.argv) != 2:
	print("Usage:\n  Please use commandLine as:\n\t python example.py xml_filename")
else:
	xml_filename = sys.argv[1]
	try:
		mydoc = minidom.parse(xml_filename)

		items = mydoc.getElementsByTagName('loc')

		match_filename = re.match('(.*).xml', xml_filename)
		txt_filename = match_filename[1] + '.txt'
		
		with open(txt_filename,"w") as f:
		    for item in items:
		       print(item.firstChild.nodeValue, file=f)
		    print("Converted!")

	except BaseException:
		print("File could not be found")

