def create_dict(data, template):
    template[data] = data
    return template

def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        if isinstance(i_element, (str, int)):
            new_list.append(create_dict(i_element, template=dict()))
        elif isinstance(i_element, dict):
            new_list.append(i_element)
        else:
            continue
    return new_list

data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)