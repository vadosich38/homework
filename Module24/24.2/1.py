import random


class Toyota:
    color = "Red"
    price = 150000
    max_speed = 200
    fact_speed = 0


car1 = Toyota()
car1.fact_speed = random.randint(0, 200)

car2 = Toyota()
car2.fact_speed = random.randint(0, 200)

car3 = Toyota()
car3.fact_speed = random.randint(0, 200)

print(car1.fact_speed, car2.fact_speed, car3.fact_speed)
