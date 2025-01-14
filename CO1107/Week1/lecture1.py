# Write a program to get 3 numbers from user, using the function
# Sum_Num , add up the first 2 numbers, and then multiply its result
# with the 3rd number by using another function called Product.

def sum_num():
    
    num1 = int(input("Please enter a Number: "))
    num2 = int(input("Please enter a Number: "))
    val = num1 + num2  
    return(val)


def product(val):
    
     num3 = int(input("Please enter a Number: "))
     finalVal = val * num3
     return(finalVal)

sumResult = sum_num()

finalResult = product(sumResult)

print ("The final result is: ", finalResult)


 
 
 
 
 