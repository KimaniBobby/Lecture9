#this function multiplies 5 by itself the number of times entered as the whole number

# i.e if the number entered is 4 the calculation is as follow 5 * 5 * 5 * 5



def factor():

    n = int(input("Please enter a whole number:"))

    fact = 1

    for factor in range (1, n+1):

        fact = fact * 5

       

    print("The power of 5^n of:",n, "is",fact)

factor()