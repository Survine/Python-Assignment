import random
random_list = []
for i in range(10):
    random_list.append(random.randint(1, 100))
maximum = max(random_list)
minimum = min(random_list)
average = sum(random_list) / len(random_list)
print("Random List:", random_list)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Average Value:", average)