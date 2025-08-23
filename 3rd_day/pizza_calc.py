print("What kind of pizza do you want?")

size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on you pizza? Y or N:")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price_to_pay = 0
if size == "S":
    price_to_pay+=15
elif size == "M":
    price_to_pay+=20
else:
    price_to_pay+=25

if pepperoni == "Y":
    if size == "S":
        price_to_pay+=2
    else:
        price_to_pay+=3

if extra_cheese == "Y":
    price_to_pay+=1

print(f"Your final bill is: {price_to_pay}")