my_dict = {"a":55,"b":56,"c":56,"d":57}
new_dict = {}
for k in my_dict.keys():
    value = my_dict[k]
    new_dict[value] = k
print(new_dict)