import requests
import json

def getFish(fish): 
    response = requests.get(f"https://www.fisheries.noaa.gov/topic/sustainable-seafood{fish.lower()}")


    data = response.json()
    return data

fishes = getFish("Dall’s Porpoise")
print(fishes) 


""" def divide(a,b):
    try: 
        result = a/b
    except ZeroDivisionError: 
        print("Cannot divide by 0")
    else: 
        print(a/b)



divide(10,0) """