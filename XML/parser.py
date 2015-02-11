#!/usr/bin/python

# use python to handle XML seems to be very easy

import xml.etree.ElementTree as ET

# core class is ElementTree.Element
# core class is ElementTree.ElementTree

tree = ET.parse('test.data')
root = tree.getroot()
text = ET.tostring(root)
#print text
#print root

# or 
# country_data_as_string = ''
# root = ET.fromstring(country_data_as_string)


# basic use
print root.tag
print root.attrib

for child in root:
    print child.tag,child.attrib

print root[0][1].text




# finding interesting elements
for neighbor in root.iter('neighbor'):
    print neighbor.attrib

for country in root.findall('country'):
    print country.find('rank').text
    print country.get('name')



# modify an XML file

# find all just search subElement
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('output.xml')

# iter search all element
for rank in root.iter('rank'):
    new_rank = int (rank.text) +1 
    print 'num is ' + str(new_rank)
    rank.text=str(new_rank)
    rank.set('update','yes')
    rank.set('color','white')
tree.write('output2.xml')



# building XML 
a=ET.Element('a')
a.attrib['len']='99'
b=ET.SubElement(a,'b')
b.attrib['age']='88'
c=ET.SubElement(a,'c')
d=ET.SubElement(c,'d')

e=ET.Comment('this is a Comment')

#print type(e)
#print type(a)


x = root.find('country')
y = root.iter('country')
print type(x)   #Element
print type(y)   #generator

x = root.findall('country')
y = root.iterfind('country')
#print type(x)  #list
#print type(y)  #generator


