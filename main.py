#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = input("What percentage tip would you like to give? ")
tip = float(tip)/100 + 1
num_people = int(input("How many people will split the bill? "))
split = round(total * tip / num_people, 2)
split = "{:.2f}".format(split)
print(f"Each person should pay ${split}")
