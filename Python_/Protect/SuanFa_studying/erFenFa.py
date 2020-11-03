# def erFenFa(list,item):
#     low = 0
#     high = len(list)-1
#
#     while low<= high:
#         mid = (low + high)//2
#         if list[mid] == item:
#             return mid
#         if list[mid] > item:
#             high = mid - 1
#         if list[mid] < item:
#             low = mid + 1
#     return None
# my_list = range(0,9999999999999)
# print (erFenFa(my_list,54654564))

def erFenfa(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (high+low)//2
        if(list[mid]==item):
            return mid
        if(list[mid]>item):
            high = mid-1
        if(list[mid]<item):
            low = mid +1
    return None

my_list = range(0,99999,2)
print(erFenfa(my_list,5556))
