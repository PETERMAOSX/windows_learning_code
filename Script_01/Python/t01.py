my_list = [1,1,1,2,2,2,3,3,3,4,4,4,4,4,5,5,5,5,5]
def solution(array):
    if(len(array) == 0):
        return 0
    index = 0
    for i in range(1,len(array)):
        if(array[index] != array[i]):
            index +=1
            array[index] = array[i]
    return index + 1
print(solution(my_list))
