# ==========================================
# Q1. Create a program that:
# 1. Opens a file "names.txt" in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names
# ==========================================
print("-"*80)
print("Question number 1 solution:")
print("-"*80)
with open("names.txt",'w') as f:
    for i in range(0,5):
        name = input("Enter the name you want to add into the file: ")
        f.write(name + "\n")
print("-"*80)

# ==========================================
# Q2. Create a program that:
# 1. Opens a file "log.txt" in append mode
# 2. Adds a new log entry (like "Program run successfully")
# 3. Opens the file in read mode and prints all logs
# ==========================================
print("-"*80)
print("Question number 2 solution:")
print("-"*80)
with open("log.txt",'a') as f:
    f.write("Program run successfully" + "\n")

with open("log.txt",'r') as file:
    print(file.read())
print("-"*80)

# ==========================================
# Q3. Create a program that:
# 1. Has a list of numbers: [5, 10, 15, 20, 25]
# 2. Uses a list comprehension to create a new list with only numbers greater than 15
# 3. Prints the new list
# ==========================================
print("-"*80)
print("Quetsion number 3 Solution: ")
print("-"*80)
old_list = [5,10,15,20,25]
new_list = [ele for ele in old_list if ele > 15]
print(new_list)
print("-"*80)

# ==========================================
# Q4. Create a Python dictionary of 3 cities and their populations. Save it to "cities.json".
# 1. Then load the JSON and print each city and its population.
# 2. Ask the user for a new city & its population - update this info in the json file.
# ==========================================
import json

print("-"*80)
print("Question number 4 solution: ")
print("-"*80)
cities = {}
for i in range(0,3):
    print(f"Enter the details for City Number {i+1}:")
    city_name = input("Enter the name of the city: ")
    population_data = float(input("Enter the population of the city in million: "))
    cities[city_name] = population_data

json_string = json.dumps(cities)
print("Saved the cities.json file successfully")
with open("cities.json","w") as file:
    file.write(json_string)

print("Reading the file cities.json and printing the content of the file 'cities.json' successfully")
with open("cities.json","r") as file:
    data = json.load(file)
    print(data)

print("Updating the json file with a new city and its population:")
city_name = input("Enter the name of the city: ")
population_data = float(input("Enter the population of the city in million: "))
cities[city_name] = population_data
with open("cities.json","w") as file:
    file.write(json.dumps(cities))
print("-"*80)

# ==========================================
# Q5. Write a program that tries to open "data.txt" in read mode. If the file does not
# exist, catch the exception and print "File not found!".
# ==========================================
print("-"*80)
print("Question no 5 solution: ")
print("-"*80)
try:
    with open("data.txt","r") as file:
        data = file.read()
        print(data)
except:
    print("File not found!")
else:
    print("File found and read the data successfully!")
finally:
    print("End of Program")
print("-"*80)