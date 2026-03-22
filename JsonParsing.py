import json

importData_toString = ('{"employees": \
                        {"employee": \
                            [{"id": "1","firstName": "Tom","lastName": "Cruise","photo": "https://jsonformatter.org/img/tom-cruise.jpg"},\
                             {"id": "2","firstName": "Maria", "lastName": "Sharapova", "photo": "https://jsonformatter.org/img/Maria-Sharapova.jpg"},\
                             {"id": "3","firstName": "Robert", "lastName": "Downey Jr.", "photo": "https://jsonformatter.org/img/Robert-Downey-Jr.jpg"}]}}')

# loads converts string to dictionary
empl_data = json.loads(importData_toString)
# print(type(empl_data))
# print(empl_data)

emp = empl_data['employees']['employee']
emp1 = empl_data['employees']['employee'][0]
emp2 = empl_data['employees']['employee'][1]
emp3 = empl_data['employees']['employee'][2]


# print(emp1['id'])
# print(emp1['firstName'])
# print(emp1['lastName'])
# print(emp1['photo'])


#validating that it finds the correct employee
for empl in emp:

    if empl['firstName'] == 'Robert':
        assert empl['id'] == '3', f'Employee id is not the same as {empl['id']}'

