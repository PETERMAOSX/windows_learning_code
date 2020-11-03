my_list = [2,5,6,8,1,4,11,12,10]
for i in range(len(my_list)):
    for j in range(len(my_list)-i-1):
        if my_list[i]>my_list[i+1]:
            temp = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1] = temp
print(my_list)