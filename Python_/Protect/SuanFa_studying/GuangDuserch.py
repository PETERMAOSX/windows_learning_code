graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anju','peggy','maoshaoxiong']
graph['alice'] = ['peggy']
graph['claire']=['thom','jonny']
graph['anju'] =[]
graph['peggy'] = []
graph['thom'] = []
graph['jonny']=[]
graph['maoshaoxiong']=[]


# search_queue = deque()
# search_queue += graph['you']




# while search_queue:
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print (person+'is a mango seller!')
#     else :
#         search_queue += graph[person]
# from collections import deque #创建一个队列
# def person_is_seller(name):
#     return name[-1] == 'm'
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if (person not in searched):
#             if person_is_seller(person):
#                 print (person + 'is a mango seller!')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
# search('you')
# from collections import deque
# def person_is_seller(name):
#     return name[-1]=='m'
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched :
#             if person_is_seller(person):
#                 print(person + ' is a seller!')
#                 return True
#             else :
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
# search('you')
# from collections import deque
#
# def person_is_seller(name):
#     return name[-1] == 'm'
# def search(name):
#     search_deque = deque()
#     search_deque += graph[name]
#     seared = []
#     while search_deque:
#         person = search_deque.popleft()
#         if person not in seared:
#             if person_is_seller(person):
#                 print (person + ' is a seller!')
#                 return True
#             else :
#                 search_deque += graph[person]
#                 seared.append(person)
#     return False
#
# search('you')

from collections import deque
def person_is_seller (name):
    return name[-1]=='m'
def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller!')
                return True
            else:
                search_deque += graph[person]
                searched.append(person)
    return False
search('you')






