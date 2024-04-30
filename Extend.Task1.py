my_list = ["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
extend_list = ["h","i","j"]
my_list[2][1][2].extend(extend_list)
print(my_list)