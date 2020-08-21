from xml.etree import ElementTree

new_data = '<cube color="blue">' \
               '<cube color="red">' \
               '</cube>' \
               '<cube color="red">' \
               '</cube>' \
           '</cube>'

new_data = ElementTree.fromstring(new_data)
count_score = {'red': 0, 'green': 0, 'blue': 0}


def count_colors(data, lvl):
    count_score[data.attrib['color']] += lvl
    lvl += 1
    for new_data in data:
        count_colors(new_data, lvl)


count_colors(new_data, 1)
print(count_score['red'], count_score['green'], count_score['blue'])
