
#! 1. Tip Calculator
# amount = float(input("Total bill amount? ")) ##float because we work with decimals
# service = input("Level of service? ").lower().strip()
# if service == "good":
#     tip_amount = amount * 0.2
# elif service == "fair":
#     tip_amount = amount * 0.15
# elif service == 'bad':
#     tip_amount = amount * 0.1
# total = amount + tip_amount
# print("Tip amount: $%.2f" % tip_amount)
# print("Total amount: $%.2f" % total)


#! 2 Tip Calculator 
# amount = float(input("Total bill amount? "))
# service = input("Level of service? ").lower().strip()
# split = int(input("Split how many ways? "))
# if service == "good":
#     tip_amount = amount * 0.2
# elif service == "fair":
#     tip_amount = amount * 0.15
# elif service == 'bad':
#     tip_amount = amount * 0.1
# total = amount + tip_amount
# total_per_person = total / split
# print("Tip amount: $%.2f" % tip_amount)
# print("Total amount: $%.2f" % total)
# print("Amount per person: $%.2f" % total_per_person)


#! 3. How many coins?
# answer = ""
# coins = 0
# while answer != "no":
#     print(f"You have {coins} coins.")
#     answer = input("Do you want another? ")
#     coins += 1
# print("oh well")


#! 4 Print a Box

# count = 0
# width = int(input('Width? '))
# height = int(input('Height? '))
# print(width * "*")
# while count < height - 2:
#     print("*" + ((width - 2) * " ") + "*")
#     count +=1
# print(width * "*")

#! 4 Print a Box
# width = int(input("Width? "))
# height = int(input("Height? "))
# num1 = 1
# while num1 <= height:
#     num2 = 1
#     stars = ""
#     while num2 <= width:
#         if num1 == 1 or num1 == height:
#             stars += "*"
#         else:
#             if num2 == 1 or num2 == width:
#                 stars += "*"
#             else:
#                 stars += " "
#         num2 += 1
#     print(stars)
#     num1 += 1


#! 5. Print a Triangle

#? solution
# count = 1
# down = 3
# while count < 9:
#     print((down * " ") + (count * '*'))
#     down -= 1
#     count += 2

#? solution
# triangle_height = int(input("Please input height of triangle: "))
# num = 1
# spaces = triangle_height - 1
# while num <= triangle_height * 2:
#     print((spaces * " ") + num * "*")
#     spaces -= 1
#     num += 2

#?solution
# height = int(input('Enter a height >> '))
# count = 0
# stars = 1
# base_width = height * 2 - 1
# while count < height:
#     star = '*' * stars
#     count += 1  # count = count + 1
#     stars += 2  # stars = stars + 2
#     print(star.center(base_width))

#? solution
# height = int(input("What is the height? "))
# i = 0
# while i < height:
#     print((height - i) * " " + (2 * (i + 1) - 1) * "*" + (height - i) * " ")
#     i += 1

#! 6. Multiplication Table. Print the multiplication table for numbers from 1 up to 10.
# num1 = 1
# while num1 <= 10:
#     num2 = 1
#     while num2 <= 10:
#         print(f"{num1} X {num2} = {num1 * num2}")
#         num2 += 1
#     num1 += 1





