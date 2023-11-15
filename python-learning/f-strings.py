letter = "Hey my name is {} and I am from {}"
name = "Saksham"
country = "India"
print(letter.format(name,country))

letter = "Hey my name is {1} and I am from {0}"
name = "Saksham"
country = "India"
print(letter.format(country,name))

text = "Hey the price is {price:.2f}"
print(text.format(price=49.0999))

print(f"Hey my name is {name} and I am from {country}") #f-strings

price = 49.099
print(f"The price is {price:.2f}")

print(f"{2*30}")