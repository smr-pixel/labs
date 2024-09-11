first_side = input("Input the length of the triangle's first side.")
second_side = input("Input the length of the triangle's second side.")
first_side = float(first_side)
second_side = float(second_side)
import math
hypotenuse = math.sqrt(first_side**2 + second_side**2)
round_hypotenuse = round(hypotenuse, 2)
hypotenuse = str(round_hypotenuse)
print("The hypotenuse is " + hypotenuse)
