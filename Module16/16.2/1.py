zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

print("Приехал медведь, теперь животные размещены так:")
zoo.insert(zoo.index('lion')+1 ,'bear')
print(zoo)

print("Прошла неделя и жираф уехал, теперь животные размещены так:")
zoo.remove('elephant')
print(zoo)