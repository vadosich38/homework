family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

for child in family_member["children"]:
    if child.get('name') == "Bob":
        print("В семье есть ребенок с именем Вов")
        f_name = child.get("surname", "Nosurname")
        print("Его фамилия:", f_name)

