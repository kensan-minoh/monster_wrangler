def another_function(a, b, *list):
    print(f"a: {a}, b: {b}, list: {list}")
    print(*list)
    print(type(list))

my_list = [10, 20, 30]
print(*my_list)
another_function(*my_list,100,1000, *my_list)

# 出力
# 10 20 30
# a: 10, b: 20, list: (30, 100, 1000, 10, 20, 30)
# 30 100 1000 10 20 30
# <class 'tuple'>

