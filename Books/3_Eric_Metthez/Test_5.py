def build_person(first_name, last_name, his_age=''):
    """return inf about person"""
    person = {'first': first_name, 'last': last_name}
    if his_age:
        person['age'] = his_age
    return person


Vova = build_person("Vladimir", "Pavluykov", 30)
Kate = build_person('Kate', 'Romanova')
print(Vova)
print(Kate)
