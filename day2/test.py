# from tabulate import tabulate
# import pandas as pd

# todo={
#         'one': 'this is first task',
#         'two':'this is second task',
#         'five':'nothing to do'
# }
# key = list(todo.keys())

# print(key)
# for key , val in todo.items():
#             print(f"{key} : {val}")

# dt = pd.DataFrame(todo)


# table = [(key , val) for key , val in todo.items()]

# a=(tabulate(table ,headers=["Taks-Name" , "Task Discription"], tablefmt="grid"))
# print(a)


lis = [x**2 for x in range(1,101,) if x%2==0]

print(lis)