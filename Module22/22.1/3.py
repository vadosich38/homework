import os

file = "search.py"
path = os.path.abspath(file)
print(path)
print(path[:5])

print(os.path.abspath(os.path.join(os.path.sep)))

