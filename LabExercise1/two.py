
# 2. Write a program that reads the length of the base and the height of a right-angled triangle
# #and prints the area. Every number is given on a separate line.

length = int(input("Enter the value of length: "))
height = int(input("Enter the height: "))

area = (length * height)//2
# the floor division // rounds the result down to the nearest whole number

print(f"The area of right angled triangle is {area} ")