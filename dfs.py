import requests
import json


def getFruity(fruit): 
    response = requests.get(f"https://www.fruityvice.com/api/fruit/family/{fruit.lower()}")
    if response.status_code != 200: 
        print("Error fetching data!")
        return None
    data = response.json()
    return data


fruit = getFruity("Rosaceae")

result = {}
for fruits in fruit:
    result.update(fruits)

print(result)
print(result["name"])

question = input("What family do you think the following fruit is?") 
print(result["name"])
if question == "Rosaceae": 
    print("YESSSS GOOD JOBB!!!!") 
else: 
    print("WRONG HAHAHHAHA") 





""" def divide(a,b):
    try: 
        result = a/b
    except ZeroDivisionError: 
        print("Cannot divide by 0")
    else: 
        print(a/b)



divide(10,0) """