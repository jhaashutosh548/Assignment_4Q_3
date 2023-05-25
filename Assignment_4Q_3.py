def square_list_func(lst):
    squared_list = list(map(lambda x: x ** 2, lst))
    return squared_list
input_list = [4, 5, 2, 9]
result = square_list_func(input_list)
print(result)