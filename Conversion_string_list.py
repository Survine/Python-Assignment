string_list = ["10", "20", "30", "40", "50", "abc", "60", "70"]
integer_list = []
for string in string_list:
    try:
        integer = int(string)
        integer_list.append(integer)
    except:
        print("Invalid Value:", string)
print(integer_list)