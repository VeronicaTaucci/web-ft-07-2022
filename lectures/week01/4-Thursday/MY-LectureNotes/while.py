
# 1. Create a program that will print from 1-10 using a while loop.
# num = 1
# while num <= 10:
#     print(num)
#     num+=1
# 2. Create a program that will print from 10-1 using a while loop.
# num = 10
# while num >= 1:
#     print(num)
#     num-=1

# 3. Create a program that prompts the user to enter a word.  The program doesn't stop asking the user to enter a word until the user enters the word "stop"

# while True:
#     inpt = input("say a word: ")
#     if inpt == "stop":
#         break

# 4a. Create a program that has a variable named username and another variabled named password with values of your choice.
# username = 'Vero'
# password = '123'
# #4b. Prompt the user for a username and then a password.
# name1 = input("username? ")
# pass1 = input("password? ")
# 4c. If the both match continue on with the program and give a welcome message.
# if name1 == username and password == pass1:
#     print('welcome')
# else:
#     print("wrong")
# 4d. If not it prompts the user for the username and password until they get it correct.
# while name1 != username and password != pass1:
#     print("wrong")
#     name1 = input("username? ")
#     pass1 = input("password? ")
# else:
#     print('welcome')
# #4e. (bonus) have a limited amount of attempts and if they reach the limit it tells the user and exits the program.

username = 'Vero'
password = '123'
login_attempt_username = "".lower()
login_attempt_password = "".lower()
attempts = 0

while (login_attempt_username != username or login_attempt_password != password) and attempts < 5:
    login_attempt_username = input('username?')
    login_attempt_password = input('password?')
    attempts += 1
    if login_attempt_username == username and login_attempt_password == password:
        print('welcome!')
    elif attempts == 5:
        print('too many attempts.')
