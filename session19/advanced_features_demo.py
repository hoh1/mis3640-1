import math

# x = float(input())
# if x > 0:
#     y = math.log(x)
# else:
#     # a special floating-point value that represents “Not a Number”.
#     y = float('nan')
# print(y)

# y = math.log(x) if x > 0 else float('nan')


# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res

def capitalize_all(t):
    return [s.capitalize() for s in t]

a = 'Babson College'
# print(capitalize_all(a))


# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#     return res

def only_upper(t):
    return [s for s in t if s.islower()]

print(only_upper(a))
