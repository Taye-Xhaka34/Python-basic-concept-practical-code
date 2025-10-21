#create a function that accepts username and age, then display the name and the age and also display the year which the user born
def user_info(name, age):
    year_born = 2024 - age
    return f"Name: {name}, Age: {age}, Year Born: {year_born}"
print(user_info("Alice", 30))