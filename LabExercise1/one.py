
# 1. Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

first_num = input("First number: ")
second_num = input("Second number: ")
third_num = input("Third number: ")

first_num = int(first_num)
second_num = int(second_num)
third_num = int(third_num)

addition = (first_num + second_num + third_num)

print(f"The sum is: {addition}")

########################################################################################
# Easy way

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))
sum_num = a+b+c
print(f"The sum of given three numbers is: {sum_num}")

