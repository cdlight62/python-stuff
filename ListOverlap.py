import random

a = random.sample(range(100), random.randrange(100))
b = random.sample(range(100), random.randrange(100))

print(sorted(a))
print(sorted(b))
print("intersect: " + str(list(set(a).intersection(b))))