students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

pairs_list = [(i_key, i_value) for i_key, i_value in students.items()]
print(pairs_list)

def students_data(dict):
    hobby_lst = []
    family_len = 0
    for i_value2 in dict.values():
        if 'interests' in i_value2:
            hobby_lst += i_value2['interests']
        else:
            print("У студента {0} {1} нет интересов".format(i_value2['name'], i_value2['surname']))
        if 'surname' in i_value2:
            family_len += len(i_value2['surname'])
        else:
            print("У студента {0} {1} нет фамилии".format(i_value2['name'], i_value2['surname']))
    return hobby_lst, family_len

hobby_list, surnames_len = students_data(students)
print("\nВсе хобби студентов: {}\nДлина всех фамилий студентов: {}".format(hobby_list, surnames_len))