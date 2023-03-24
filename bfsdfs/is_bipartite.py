# use dict `color ={} ` to keep track of seen + status

    def isBipartite(self, graph):
        color = {}
        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True


# We have two lists of e-commerce data, clients and orders. Working with these lists, write a function that outputs a list of orders with the client name/state.




import heapq
from heapq import heappop, heappush


'''
Given the same input as in Question 1, print out the sum of all order values for the top 10 clients, in decreasing order of order total. For example, given the above test data, one entry in the output would be:

   {
       clientId: 1,
       clientName: "Acme, Inc.",
       clientState: "NY",
       total: "2010.38",
   },
'''

clients = [
    {
        'ClientId': 1,
        'Name':     "Acme, Inc.",
        'State':    "NY",
    },
    {
        'ClientId': 2,
        'Name':     "Widgets, LLC",
        'State':    "CA",
    },
    {
        'ClientId': 3,
        'Name':     "Stuff Store",
        'State':    "TX",
    },
]

orders = [
    {
        'OrderId':  1,
        'ClientId': 1,
        'Date':     "2022-04-01",
        'Total':    2000.15,
    },
    {
        'OrderId':  2,
        'ClientId': 1,
        'Date':     "2022-08-10",
        'Total':    10.23,
    },
    {
        'OrderId':  3,
        'ClientId': 1,
        'Date':     "2022-09-04",
        'Total':    17.00,
    },
    {
        'OrderId':  4,
        'ClientId': 2,
        'Date':     "2022-09-23",
        'Total':    1002.15,
    },
]

# The expected output is:
clientOrders = [
    {
        'OrderId':        1,
        'ClientId':       1,
        'Date':           "2022-04-01",
        'Total':          2000.15,
        'ClientName':     "Acme, Inc.",
        'ClientState':    "NY",
    },
    {
        'OrderId':        2,
        'ClientId':       1,
        'Date':           "2022-08-10",
        'Total':          10.23,
        'ClientName':     "Acme, Inc.",
        'ClientState':    "NY",
    },
    {
        'OrderId':        3,
        'ClientId':       1,
        'Date':           "2022-09-04",
        'Total':          17.00,
        'ClientName':     "Acme, Inc.",
        'ClientState':    "NY",
    },
    {
        'OrderId':        4,
        'ClientId':       2,
        'Date':           "2022-09-23",
        'Total':          1002.15,
        'ClientName':     "Widgets, LLC",
        'ClientState':    "CA",
    },
]

# assume all client id in orders are valid

# def sol1(clients, orders):
#     client_dic = dict()
#     for client in clients:
#         client_dic[client['ClientId']] = client

    
#     res = []
#     for order in orders:
#         clientId = order['ClientId']
#         temp = order
#         temp['ClientName'] = client_dic[clientId]['Name']
#         temp['ClientState'] = client_dic[clientId]['State']
#         res.append( temp )


#     return res

# print (sol1(clients, orders))


# def sol2(clients, orders, top = 2):
#     client_dic = dict()
#     for client in clients:
#         client_dic[client['ClientId']] = client

#     res = {}
#     for order in orders:
#         clientId = order['ClientId']
        
#         if clientId in res:
#             res[clientId]['total'] += order['Total']
#         else:
#             temp = {'clientId': clientId}
#             temp['clientName'] = client_dic[clientId]['Name']
#             temp['clientState'] = client_dic[clientId]['State']
#             temp['total'] = order['Total']
#             res[clientId] = temp 

#     lst = sorted(res.values(), key = lambda x: x['total'], reverse=True)
#     if len(lst) > top:
#         return lst[:top]
#     return lst


# print(sol2(clients, orders))



def sol3(clients, orders, top = 2):
    client_dic = dict()
    for client in clients:
        client_dic[client['ClientId']] = client

    heap = [] # (total, client id)

    res = {}
    for order in orders:
        clientId = order['ClientId']
        
        if clientId in res:
            res[clientId]['total'] += order['Total']
        else:
            temp = {'clientId': clientId}
            temp['clientName'] = client_dic[clientId]['Name']
            temp['clientState'] = client_dic[clientId]['State']
            temp['total'] = order['Total']
            res[clientId] = temp 

        
        if len(heap) < top:
            heappush(heap, (res[clientId]["total"], clientId))
        else:
            cur_min = heap[0]
            if cur_min[0] < res[clientId]['total']:
                heappop(heap)
                heappush(res[clientId]['total'], clientId)

    print ('heap')
    # return heap

print(sol3(clients, orders))