list = []#creates an empty list thet will store the numbers entered by the user

num = int(input('How many numbers: '))#the user determines how many times they should be prompted to enter a number

for n in range(num):

    numbers = int(input('Enter number: '))

 

    list.append(numbers)#enters user entered numbers into the list


print("Sum of numbers in the list is :", sum(list))

    


