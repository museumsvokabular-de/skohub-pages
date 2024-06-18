import rdflib
import lxml.etree

# load ackerbau.rdf with lxml.etree
tree = lxml.etree.parse("ackerbau.rdf")
root = tree.getroot()
skosList = ["{http://www.w3.org/2004/02/skos/core#}narrower",
            "{http://www.w3.org/2004/02/skos/core#}broader",
            ]
#iterate over all elements of root
for element in root.iter():
    if element.tag == "{http://www.w3.org/2004/02/skos/core#}Concept":
        uuid= element.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
        element.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", uuid.replace(" ", ""))
        for subElement in element.iter():
            if subElement.tag in skosList:
                subElement.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", subElement.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource").replace(" ", ""))

#save the modified tree
tree.write("ackerbau_modified.rdf", pretty_print=True, encoding="utf-8")

# fix encoding issues
# to be finished
"""
with open("ackerbau_modified.rdf", "r") as file:
    text = file.read()
    text = text.replace("�", "ä")
    text = text.replace("�", "ö")
    text = text.replace("�", "ü")
    text = text.replace("�", "Ä")
    text = text.replace("�", "Ö")
    text = text.replace("�", "Ü")
    text = text.replace("�", "ß")
with open("ackerbau_modified.rdf", "w") as file:
    file.write(text)
"""

# load "ackerbau.rdf" as rdf xml and convert to ttl with rdflib. use urlencode
g = rdflib.Graph()
g.parse("ackerbau_modified.rdf", format="xml")
g.serialize("ackerbau_modified.ttl", format="turtle")




