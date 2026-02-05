cities = ['Seattle','Berlin','New York','Rio','Tokyo','London']
print(cities)
begcities = cities[0:2]
print(f"\nThe first two items in the list are: {begcities[0]}, {begcities[1]}.")
print("Or represented as a loop:")
print("The first two items in the list are:")
for beg in begcities:
    print(beg)
print("And finally, the first two items represented as a list:")
print(begcities)
print(f"\nThe middle two items in the list are: {cities[2]}, {cities[3]}.")
print(f"\nThe first and last items in the list are: {cities[0]}, {cities[-1]}.")
print("\nI will now examine tuples, please join me on this journey...")
foods = ('Sandwhich','Salad','Shakshouka','Durian','Kokorec')
print(foods)
for food in foods:
    print(food)
print("\nAPPARENTLY, our choice of adventurous foods was a bit too much for our customers. Let's try less adventure - more fat!")
print("\nOG foods")
for food in foods:
    print(food)
foods = ('Sandwhich','Salad','Shakshouka','Cheeseburger','Loco Moco')
print("\nNew Menu")
for food in foods:
    print(food)