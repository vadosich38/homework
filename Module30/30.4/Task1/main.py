from typing import Dict, Union, List

grades: List[Dict[str, Union[str, int]]] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41},
                                      {'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37},
                                      {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
                                      {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2},
                                      {'name': 'Mary', 'score': 63}, {'name': 'Ronald', 'score': 15},
                                      {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
                                      {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13},
                                      {'name': 'Lloyd', 'score': 52}, {'name': 'Vanessa', 'score': 6},
                                      {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
                                      {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9},
                                      {'name': 'Bruce', 'score': 68}, {'name': 'Ramona', 'score': 64},
                                      {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
                                      {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94},
                                      {'name': 'Sandra', 'score': 40}]

print("Минимальное количество очков: ", min(grades, key=lambda paar: paar['score']))
print("Максимальное количество очков: ", max(grades, key=lambda paar: paar['score']))