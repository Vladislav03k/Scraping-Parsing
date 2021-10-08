def my_func(name, surname, year_of_birth, city, email, phone_number):
    return print(f"Name: {name}, surname: {surname}, year_of_birth: {year_of_birth}, city: {city}, email: {email}, phone_number: {phone_number}")
my_func(
    name = input("Name:"),
    surname = input("Surname:"),
    year_of_birth = input("year_of_birth:"),
    city = input('city:'),
    email = input('email:'),
    phone_number = input('phone_number:')
)