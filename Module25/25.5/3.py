class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


data = MyDict({"a": 0, "c": 1})
data["ac"] = 12
print(data.get("d"))
