#1
numbers = [i for i in range(9)]
print(numbers)

#2
squares = [x**2 for x in range(7)]
print(squares)

#3
even_nums = [m for m in range(10) if m % 2 == 0]
print(even_nums)

#4
name_list = ['Ivan', 'Aleksander', 'Milana']
lengths = [len(name) for name in name_list]
print(lengths)

#5- (здесь не поняла с чего это он мне не выдаёт по порядку)
nums = [111, 222, 222, 333, 444, 555]
unique_nums = list(set(nums))
print(unique_nums)

#6
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_even_numbers)

#7
list1 = ['A', 'B']
list2 = [1, 2, 3]
combined_list = [(x, y) for x in list1 for y in list2]
print(combined_list)
