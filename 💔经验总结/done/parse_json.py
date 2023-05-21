ex = [
    {'type': 'start'},
    {'type': 'field-name', 'val': 'a'},
    {'type': 'start'},
    {'type': 'field-name', 'val': 'b'},
    {'type': 'start'},
    {'type': 'field-name', 'val': 'x'},
    {'type': 'number', 'val': 1},
    {'type': 'end'},
    {'type': 'field-name', 'val': 'c'},
    {'type': 'start'},
    {'type': 'field-name', 'val': 'y'},
    {'type': 'number', 'val': 2},
    {'type': 'end'},
    {'type': 'end'},
    {'type': 'end'},
]

print('here')


# def sol(inputlist, i=0):
#     field_name = None

#     res = {}

#     while (i < len(inputlist)):
#         t = inputlist[i]
#         print(i, i < len(inputlist), t['type'], res)
#         if t['type'] == 'start':
#             if field_name is not None:
#                 tmp, index = sol(inputlist, i + 1)
#                 i = index
#                 print('i = index + i', i)
#                 res[field_name] = tmp
#             else:
#                 res, end = sol(inputlist, i + 1)
#         elif t['type'] == 'end':
#             return res, i
#         elif t['type'] == 'field-name':
#             field_name = t['val']
#         else:
#             res[field_name] = t['val']
#         i += 1
#     return res


def sol(inputlist):
    field_name = None
    i = 0
    res = {}

    while (i < len(inputlist)):
        t = inputlist[i]
        # print(i, i < len(inputlist), t['type'], res)
        if t['type'] == 'start':
            if field_name is not None:
                tmp, index = sol(inputlist[i + 1:])
                i = index + i + 1
                # print('i = index + i', i)
                res[field_name] = tmp
            else:
                res, end = sol(inputlist[i + 1:])
        elif t['type'] == 'end':
            return res, i
        elif t['type'] == 'field-name':
            field_name = t['val']
        else:
            res[field_name] = t['val']
        i += 1
    return res


print('sol', sol(ex))
