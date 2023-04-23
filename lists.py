"""
coolection  data types(list) are used to store MULTIPLE data(items) in ONE Variable
"""

# to create a list we use [] or list()

my_list = ['this is a string', 2500, True, 2.5]


my_to_do_list = ['1) Clean the flat', '2) go grocery shopping', '3) cook', '4) Eat']

my_list2 = list()

colors = ['yellow', 'black', 'red', 'green']


print(colors)


# accessing an item of list, we use indexing -> colors[index]
colors = ['yellow', 'black', 'red', 'green']

#          0          1        2      3

print(colors[-1+1])


# adding an item to the end of a list -> append()

colors.append('orange')

print(colors)

# deleting an item from a list -> pop() removes the last item in the list.

colors.pop()
print(colors)


# deleting a list item at a given index -> remove('item')
colors.remove('yellow')
print(colors)
# adding an elemnt at a given index -> insert(index)

colors.insert(0, 'blue')
print(colors)

"""
using the input() function, ask the admin to enter a list of salaries
separated by a comma
and add 500 to each salary and diplay the salary at the of the list.

example: 1000,500,4500,2000,6000
"""

# salary = [2000, 1000, 4500]
# print(salary[1]*2)

# salaries = input('Enter amounts: ')

# list_salaries = salaries.split(',')

# int_from_list = []

# for i in list_salaries:
#     i = int(i)
    
#     int_from_list.append(i*2)

# print(int_from_list)



"""
append()
pop()

remove('yellow)
insert(0, 'blue')
"""















































