my_list = [10,20,60,30,20,40,30,60,70,80]
new_lest = []
for i in range(len(my_list)):
    if my_list[i] in my_list[i+1:]:
        new_lest.append(my_list[i])
print(new_lest)

#Роҳи дуюми ҳали ин масъала
# my_list = [10,20,60,30,20,40,30,60,70,80]
# new_list = []
# duplicat_list = []
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
#     else:
#         duplicat_list.append(i)
# print(duplicat_list)