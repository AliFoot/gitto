to_minutes = 24*60
my_age = 365*22+5
name_of_unit = "minutes"



def days_to_units(num_of_days) :
    print(f"{num_of_days} days are {num_of_days * to_minutes} {name_of_unit}")


days_to_units(35)
days_to_units(46)
days_to_units(58)

print(f"My age in {name_of_unit} is {my_age * 3600} {name_of_unit}.")
print("All good!")
