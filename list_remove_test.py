colors = ['green', 'blue', 'purple', 'orange', 'blue']
print(colors)
colors.remove('blue')
print(colors)

# 出力
# ['green', 'blue', 'purple', 'orange', 'blue']
# ['green', 'purple', 'orange', 'blue']

colors = ['green', 'blue', 'purple', 'orange', 'blue']
print(colors)
removed_list = [color for color in colors if color != 'blue']
print(removed_list)

# 出力
# ['green', 'blue', 'purple', 'orange', 'blue']
# ['green', 'purple', 'orange']

my_list = [ num for num in range(10) if num % 3 == 0 ]
print(my_list)