motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

#Using append

motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

#Using pop0
last_owned = motorcycles.pop()
print(f"the last motorcycle I owned was a {last_owned.title()}")
print(motorcycles)

#Remove
motorcycles = ['ducati', 'yamaha', 'suzuki']
motorcycles.remove('ducati')
print(motorcycles)