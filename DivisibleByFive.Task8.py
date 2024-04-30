div_list = [12,75,150,180,145,525,50]
for i in range(len(div_list)):
    if div_list[i]>=500:
        break
    if div_list[i]>150:
        continue
    if div_list[i]%5==0:
        print(div_list[i])