
#! ### 1. Find the smallest number
# Write a function `smallest` that accepts a List of numbers as an argument.
# It should return the smallest number in the List.
# nums = [8,1, 2, 3, 4, 5, 6]
# def smallest(numList):
#     num1 = numList[0]
#     for i in numList:
#         if i< num1:
#             num1 = i
#     return num1

# print(smallest(nums))

#! ### 2. Find the largest number
# Write a function `largest` that accepts a List of numbers as an argument.
# It should return the largest number in the List.
# nums = [8, 1, 2, 3, 4, 5, 6,24]
# def max_num(numList):
#     num1 = numList[0]
#     for i in numList:
#         if i > num1:
#             num1 = i
#     return(num1)
# print(max_num(nums))

#!### 3. Find the shortest String
# Write a function `shortest` that accepts a List of Strings as an argument.
# It should return the shortest String in the List.
# list = ["monday", "tuesday", "wednesday", "short"]
# def shortest_list(stringList):
#     newString = stringList[0] #short
#     for i in stringList:
#         if len(i) < len(newString):
#             newString = i
#     return newString
# print(shortest_list(list))

#!### 4. Find the longest String
# Write a function `longest` that accepts a List of Strings as an argument.
# It should return the longest String in the List.
# list = ["monday", "tuesday", "wednesday", "this_is_the_longest"]
# def longest(strinList):
#     list2 = []
#     for i in strinList:
#         if len(i) > len(list2):
#             list2 = i
#     return list2
# print(longest(list))


#! Write a function that takes a number as an input.
# Have it create an empty array and then push a string into the array as many
# times as the input number. If the input is anything other than a positive
# integer return an empty array
#
# Name the function "finalFunction"


# def finalFunction(inp):
#     myArray = []
#     i = 0 
#     while i < inp:
#         myArray.append("string")
#         i+=1
#     print(myArray)
#     return myArray

# finalFunction(4)

#! Return 'hello' if num is 1, 'world' if num is 2, otherwise return 'bye'

# def selectNum(num):
#     if num == 1:
#         print('hello')
#         return 'hello'
#     elif num ==2:
#         print('world')
#         return 'world'
#     else:
#         print('bye')
#         return 'bye'
# selectNum(3)
# Push 10 'hello' strings into the array using a for loop, then return it



arr = []

# def pushHello(inp):
#         i = 0
#         while i < inp:
#             arr.append("Hello")
#             i+=1
#         print(arr)
#         return arr

# pushHello(10)
#! Empty this array using a while loop and return it
# arr = ['hello', 'hello', 'hello', 'hello', 'hello',
#        'hello', 'hello', 'hello', 'hello', 'hello']
# def emptyArray(arr1):
#     while len(arr1) !=0:
#         arr1.pop()
#     print(arr1)
#     return arr1
# emptyArray(arr)


#! Push the string "hello" into the array and return the array
arr = [1, 'adam']
# def newArr(arr1):
#     arr1.append('hello')
#     print(arr1)
#     return arr1
# newArr(arr)
#! Remove the last element from the array and return the array
arr = [1, 'adam']
# def newArr(arr1):
#     arr1.pop()
#     print(arr1)
#     return arr1
# newArr(arr)

#! Return the length of the array
arr = [1, 'adam']
# def len1(arr1):
#     print(len(arr1))
#     return len(arr1)
# len1(arr)
#! Return the index of item "adam" in the array
arr = [1, 'adam']
# def index1(arr1):
#     print(arr1.index('adam'))
#     return arr1.index('adam')
# index1(arr)