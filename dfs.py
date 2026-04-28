import requests
import json


def getFruity(fruit): 
    response = requests.get(f"https://www.fruityvice.com/api/fruit/all")
    if response.status_code != 200: 
        print("Error fetching data!")
        return None

    data = response.json()
    print(data)

    
fruit = getFruity("apple")
print(fruit)


""" def divide(a,b):
    try: 
        result = a/b
    except ZeroDivisionError: 
        print("Cannot divide by 0")
    else: 
        print(a/b)



divide(10,0) """