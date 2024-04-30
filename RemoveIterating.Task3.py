number_list = [10,20,30,40,50,60,70,80,90,100]
my_list=[]
for i in range(len(number_list)):
    if number_list[i]<=50:
        my_list.append(number_list[i])
print(my_list)