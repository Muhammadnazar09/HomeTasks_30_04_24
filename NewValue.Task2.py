list1 = [5, 10, 15, 20, 25, 50, 20]
cnt=0
for i in range(len(list1)):
    if list1[i]==20:
        list1[i]=200
        cnt+=1
    if cnt>1:
        list1[i]=20
print(list1)


# list1 = [5, 10, 15, 20, 25, 50, 20]
# value=list1.index(20)
# list1[value]=200
# print(list1)