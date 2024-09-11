amount = input("Enter a distance or weight amount.")
split_amount = amount.split(' ')
number = split_amount[0]
unit = split_amount[1]

if unit == "cm":
    ans = float(number)/2.54
    n_unit = "in"
elif unit == "in":
    ans = float(number)*2.54
    n_unit = "cm"
elif unit == "yd":
    ans = float(number)/1.0936133
    n_unit = "m"
elif unit == "m":
    ans = float(number)*1.0936133
    n_unit = "yd"
elif unit == "oz":
    ans = float(number)*28.3495231
    n_unit = "gm"
elif unit == "gm":
    ans = float(number)/28.3495231
    n_unit = "oz"
elif unit == "lb":
    ans = float(number)/2.20462262
    n_unit = "kg"
elif unit == "kg":
    ans = float(number)*2.20462262
    n_unit = "lb"
else:
    print("Invalid input")
ans = float(ans)
number = float(number)
round_number = round(number, 2)
round_ans = round(ans, 2)
number = str(round_number)
ans = str(round_ans)
print(number + " " + unit + " = " + ans + " " + n_unit)