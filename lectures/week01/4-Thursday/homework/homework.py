# # Homework
# ## Iterative Programming

#! #### 1. Multiply Vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:
# [2, 4, 5] x[2, 3, 6] = [4, 12, 30]
list1 = [2, 4, 5]
list2 = [2, 3, 6]
list3 = []
#? for loop
# for num1,num2 in zip(list1,list2):
#     list3.append(num1*num2)
# print(list3)
#? while loop
# index = 0
# while index < len(list1):
#     list3.append(list1[index] * list2[index])
#     index+=1
# print(list3)

#! #### 2. Matrix Addition.
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:
a = [[1, 3],
     [2, 4]]
b = [[5, 2],
     [1, 0]]

c = [[0, 0],
     [0, 0]]

i = 0
j = 0

# while i < len(a):
#     while j < len(a):
#         c[i][j] = a[i][j] + b[i][j]
#         j+=1
#     j = 0
#     i+=1

# print(c)


#? for loop
# a = [[1, 3],
#      [2, 4]]
# b = [[5, 2],
#      [1, 0]]

# c = []

# for i in range(len(a)):
#     v = []
#     for j in range(len(a)):
#         v.append(a[i][j] + b[i][j])
#     c.append(v)

# print(c)
#! #### 3. Matrix Addition II
# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.
# a = [[1, 3, 6],
#      [2, 4, 7],
#      [5, 9, 8]]
# b = [[5, 3, 0],
#      [4, 2, -1],
#      [1, -3, -2]]

# c = [[0, 0, 0],
#      [0, 0, 0],
#      [0, 0, 0]]
# i = 0
# j = 0
# while i < len(a):
#     while j < len(a):
#         c[i][j] = a[i][j] + b[i][j]
#         j+=1
#     j = 0
#     i+=1

# print(c)
#? for loop
# a = [[1, 3, 6],
#      [2, 4, 7],
#      [5, 9, 8]]
# b = [[5, 3, 0],
#      [4, 2, -1],
#      [1, -3, -2]]

# c = []
# for i in range(len(a)):
#     v = []
#     for j in range(len(a)):
#         v.append(a[i][j] + b[i][j])
#     c.append(v)

# print(c)
#! #### 4. De-dup
# Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.
#? build in function
# nums = [2, 2, 3, 3, 5, 5, 7, 7]

# de_dup = []

# for x in nums:
#     if x not in de_dup:
#         de_dup.append(x)

# print(de_dup)

#?loop
#! #### 5. Leetspeak

# Given a paragraph of text as a String, print the paragraph in [leetspeak](https: // en.wikipedia.org/wiki/Leet).

# To translate a String to leetspeak, you need to replace make the following character replacements(treat all input characters as uppercase):

# | Letter | Translates To |
# |: ------: | : -------------: |
# | A | 4 |
# | E | 3 |
# | G | 6 |
# | I | 1 |
# | O | 0 |
# | S | 5 |
# | T | 7 |

# Example: If your program is given the String `"I am a leet programmer"`, it should print `"1 4m 4 l337 pr0gr4mm3r"` as the leetspeak translation

# #### 6. Long-long Vowels

# Given a word as a string, print the result of extending any long vowels to the length of 5.

# Examples:

# ```
# Good = > Goooood
# Cheese = > Cheeeeese
# Man = > Man
# Spoon = > Spooooon
# ```

# #### 7. Caesar Cipher

# Given a string, print the Caesar Cipher ( or ROT13) of that string. What is Caesar Cipher? [Learn about it here](http: // practicalcryptography.com/ciphers/caesar-cipher/).

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"


# ## Large

# ### Matrix Multiplication
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix.

# How do you multiple two matrices?



#! to do list
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

# 1. pet the cat
# 2. go to work
# 3. shop for groceries
# 4. go home

# ask user if they want to add a todo list item

# running = True
# while running:
#     # print out menu
#     index = 0
#     while index < len(todos):
#         print(f' {index+1}. {todos[index]}')
#         index += 1

#     keep_running = input('Do you want to add an item? Y or N >> ')

#     if(keep_running.lower() == 'n'):
#         running = False
#     else:
#         # ask for and input
#         new_todo = input('enter a new todo >>')
#         # append it to our list
#         todos.append(new_todo)



#!
a = [[2,3,4,],[4,7,9,6],[9,3,2,1]]
outer = 0
while outer < len(a):
    print(a[outer])
    outer +=1
                # [2, 3, 4]
                # [4, 7, 9, 6]
                # [9, 3, 2, 1]


#!Multiplication Table
# num1 = 1
# num2 = 1
# while num1 < 11:
#     while num2 < 11:
#         result = num1 * num2
#         print(num1, "X", num2, "=", result)
#         num2+=1
#     num2 = 1
#     num1+=1

#! days of the week
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5','Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# num1 = 0
# num2 = 0
# while num1 < len(weeks):
#     print(f'<<<<{weeks[num1]}>>>>')
#     while num2 < len(days):
#         print(days[num2])
#         num2+= 1
#     num2 = 0
#     num1+=1
