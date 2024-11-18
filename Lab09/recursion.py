
def product_of_digits(x):
    #remove negative sign if any
    x = abs(x)
    #Check if single digit
    #recursive until each digit is multiplied
    if x < 10:
        return x
    else:
        return (x % 10) * product_of_digits(x // 10)

def array_to_string(a, index):
    #base case, when list ends
    if index == len(a):
        return ""
    
    #variable, converts to string, holds current integer
    integer = str(a[index])

    #if last value, return the integer
    #else return integer and recursive to next in list
    if index == len(a)-1:
        return integer
    else:
        return integer + ", " + array_to_string(a, index + 1)

def log(base, value):
    #raise error if value and base are invalid
    if value <= 0 or base <= 1:
        raise ValueError("Value must be greatere than 0, and base must be greater than 1")
    
    #base case, if value is less than base function ends
    #else recursive until base case
    #add 1 because of base case
    if value < base:
        return 0
    else:
        return 1 + log(base, value // base)
        

print(product_of_digits(-12))
print(array_to_string([1, 2, 3, 4], 0))
print(log(10, 123456))
print(log(2, 64))
print(log(10, 4567))