from xml.etree import ElementTree

tree = ElementTree.parse('Test_3.7.2_example.xml')

print('-------0--------')
print(tree)

print('-------1--------')
root = tree.getroot()
print(root)

print('-------2--------')
print(root.tag, root.attrib)

print('-------3--------')
for child in root:
    print(child.tag, child.attrib)

print('-------4--------')
print(root[0][0])
print(root[0][0].tag)
print(root[0][0].attrib)
print(root[0][0].text)

print('-------5--------')
for elements in root.iter('lastName'):
    print(elements)

print('-------6--------')
for elements in root.iter('scores'):
    sum_score = 0
    for element in elements:
        sum_score += float(element.text)

    print(sum_score)

print('-------7--------')
tree.write('Test_3.7.2_example_copy.xml')

print('-------8--------')
# https://stepik.org/lesson/24474/step/2?unit=6779
# 3:20
