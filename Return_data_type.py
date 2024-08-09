def get_data_type(data):
    return type(data)

print(get_data_type(10))
print(get_data_type(3.14))
print(get_data_type(True))
print(get_data_type("Hello"))
print(get_data_type([1, 2, 3]))
print(get_data_type((1, 2, 3)))
print(get_data_type({1, 2, 3}))
print(get_data_type({"one": 1, "two": 2, "three": 3}))