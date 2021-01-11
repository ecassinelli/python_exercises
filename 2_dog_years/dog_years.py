human_years = float(input("Input human years: "))
dog_years = 0

if human_years < 2:
    dog_years = human_years * 10.5
    print(dog_years)
elif human_years >= 2:
    dog_years = 2*10.5 + (human_years-2) * 4
    print(dog_years)
else: 
    print("Error: please enter a positive number greater than 0")