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
print(fruit)

newdict = {fruits['id']: fruits['name'] for fruits in fruit}
print(newdict)

guesses = []
question = input("Guess what fruits are in the Rosaceae family!!!!")
if question in newdict.values(): 
    print("YESSS GOOD JOBBBBB")
elif question not in newdict.values(): 
    print("wrong :( try again")
    print(question)

while True: 
    hm = input("Can you guess more???")
    if hm in newdict.values(): 
        print("YAYYAYAAYA GOOD JOBBBBB")
    elif hm == "no": 
        print("awh...okay :(((")
        break
    elif hm not in newdict.values(): 
        print("grrrr NOOOOOO")

""" result = {}
for fruits in fruit:
    result.update(fruits)

print(result)
print(result["name"])

question = input("What family do you think the following fruit is?") 
if question == "Rosaceae": 
    print("YESSSS GOOD JOBB!!!!") 
else: 
    print("WRONG HAHAHHAHA")  """





""" def divide(a,b):
    try: 
        result = a/b
    except ZeroDivisionError: 
        print("Cannot divide by 0")
    else: 
        print(a/b)



divide(10,0) """