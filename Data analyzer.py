print("THIS IS AN INFORMATION ANALYZER")
name = input("What is your Name: ")
gender = input("Male or Female: ")
address = input("Where do you live: ")
birth_year = input("What year were you born: ")
age = 2023 - int(birth_year)
primary_school = input("What primary school did you attend: ")
secondary_school = input("What secondary school did you attend: ")
bio = input("Tell us a bit about yourself: ")

print("THIS IS THE INFORMATION THAT WHOULD STORED.")
print("----------------------------------------------------------")
print("                         RESULT                            ")
print("----------------------------------------------------------")
print(" NAME: ", name)
print(" GENDER: ", gender)
print(" ADDRESS: ", address)
print(" AGE: ", age)
print(" PRIMARY SCHOOL: ", primary_school)
print(" SECONDARY SCHOOL: ", secondary_school)
print(" SECONDARY SCHOOL: ", secondary_school)
print(" BIO: ", bio)
print("----------------------------------------------------------")
print("----------------------------------------------------------")

info = {'NAME': name, 'GENDER': gender, 
        'ADDRESS': gender, 'BIRTH_YEAR': birth_year, 
        'AGE': age, 'PRIMARY_SCHOOL': primary_school, 
        'SECONDARY_SCHOOL': secondary_school,
        'BIO': bio}
task = input("TO Search or change/Add info (Search/Change): ").lower()
if task == "search":
    search = input('Search: ')
    print(info.get(search))
elif task == "change":
    ans = input('Information Name: ')
    ans2 = input('Information: ')
    info[ans] = ans2
else:
    print("Index not supported")

