from cat_class import *

# Initialize a Cat object -
cat = Cat()

# Cat name
print(cat.name)

# To reassign name
fluffy_cat_instance = Cat('Tiger')
print(fluffy_cat_instance.name)

print(cat.stretch())
print(cat.jumps())
print(cat.eat(', give me food'))
print(cat.pur())
print(cat.sleep())