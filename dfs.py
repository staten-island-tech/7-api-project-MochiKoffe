import requests
import json

def getFish(fish): 
    response = requests.get(f"https://www.fisheries.noaa.gov/topic/sustainable-seafood{fish.lower()}")
    if response.status_code != 200: 
        print("Error fetching data!")
        return None

    data = response.json()
    return data

fishes = getFish("Alaska Snow Crab")
print(fishes) 