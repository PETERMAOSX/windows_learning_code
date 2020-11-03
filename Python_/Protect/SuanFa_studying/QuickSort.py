# def quickSort(arr):
#     if(len(arr)<2):
#         return arr
#     else :
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#         greater = [i for i in arr[1:] if i > pivot]
#     #return quickSort(less) + [pivot] + quickSort(greater)
#     return quickSort(less)+[pivot]+quickSort(greater)
#
# print (quickSort([10,5,41,25,55,9]))
# def num():
#     a = []
#     for i in range(0,11):
#         a.append(i)
#     return a
#
# print(num())
# b = 9
# a = [i for i in range(1,11) if b<5]
# print(a)

# def quickSort(arr):
#     if (len(arr)<2):
#         return arr
#     else :
#         pivot = arr[0]
#         less = [i for i in arr if i<pivot]
#         greater = [i for i in arr if i>pivot]
#     return quickSort(less) + [pivot] + quickSort(greater)
#
# print (quickSort([10,58,44,665,22,111]))
def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
    return quicksort(less)+[pivot]+quicksort(greater)
my_list = [555,22,55,11,432,545,2423,64646,113213,33,553,112,335]
print (quicksort(my_list))
