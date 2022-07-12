
#! while loop
# def print_to_n(n):
#     count = 0
#     while count < n:
#         count+=1
#         print(count)

#! recursion
def print_up_to(n):
    
    
    #base
    if n>0:
        print_up_to(n-1)
        print(n)


## print_up_to(5) will result in -->callstack:

#print_up_to(0)     #6
#print_up_to(1)     #5  --> #7 print(1)
#print_up_to(2)     #4  --> #8 print(2)
#print_up_to(3)     #3  --> #9 print(3)
#print_up_to(4)     #2  --> #10 print(4)
#print_up_to(5)     #1  --> #11 print(5)
