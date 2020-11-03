# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index=0
#     for i in range(1,len(arr)):
#         if (arr[i]< smallest):
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         #newArr.append(arr.pop(smallest))
#         newArr.append(arr.pop(smallest))
#     return newArr
# print (selectionSort([5,3,6,2,10]))

def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if (arr[i]<smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findsmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr



print (selectionSort([45,55,899,621,455,233,66]))