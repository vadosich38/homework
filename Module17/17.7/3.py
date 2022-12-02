import random

team1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [team1[x] if team1[x] > team2[x] else team2[x] for x in range(20)]
#winners = ["К1" if team1[x] > team2[x] else "К2" for x in range(20)]
print("Команда 1:", team1)
print("Команда 2:", team2)
print("Победители:", winners)