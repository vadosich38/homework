server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for key, value in server_data.items():
    print(key)
    for key1, value1 in value.items():
        print(" ", key1, ":", value1)