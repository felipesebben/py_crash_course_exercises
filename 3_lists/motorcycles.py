motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles = ['aprilla','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('ducati')

print(motorcycles)

motorcycles.insert(0, 'aprilla')
print(motorcycles)

motorcycles = ['aprilla','yamaha','suzuki','honda']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['aprilla','yamaha','suzuki','honda']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['aprilla','yamaha','suzuki','honda']
last_owned = motorcycles.pop()

print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['aprilla','yamaha','suzuki','honda']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['aprilla','yamaha','suzuki','honda']
motorcycles.remove('aprilla')
print(motorcycles)

motorcycles = ['aprilla','yamaha','suzuki','honda']
too_expensive = 'aprilla'
motorcycles.remove('aprilla')
print(f"\nA {too_expensive.title()} is too expensive for me.")
