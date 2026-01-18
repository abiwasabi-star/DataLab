def sum(a, b): #arguments
    return a+b


c = sum(90, 12) #params
print(c)
c = 102

def square_sum():
    x = float(input("Enter value for x: "))
    y = float(input("Enter value for y: "))
    
    result = (x + y) * (x + y)
    print("Result:", result)

# calling the function
square_sum()
