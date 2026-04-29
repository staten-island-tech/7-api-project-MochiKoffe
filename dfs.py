import requests
import json


def getFruity(fruit): 
    response = requests.get(f"https://www.fruityvice.com/api/fruit/family/{fruit.lower()}")
    if response.status_code != 200: 
        print("Error fetching data!")
        return None

    data = response.json()
    print(data)
    
fruit = {getFruity("Rosaceae")}

family = {}
for index, item in enumerate(fruit):
    if item not in family: 
        "name" == fruit["name"]


print(family["name"])




""" def divide(a,b):
    try: 
        result = a/b
    except ZeroDivisionError: 
        print("Cannot divide by 0")
    else: 
        print(a/b)



divide(10,0) """