import requests
import json
import random
import tkinter
from tkinter import *


def getFruity(fruit): 
    response = requests.get(f"https://www.fruityvice.com/api/fruit/family/{fruit.lower()}")
    if response.status_code != 200: 
        print("Error fetching data!")
        return None
    data = response.json()
    return data


def checking(): 
    if answers: 
        guess = Enter.get()
        if guess in answers:
            Checked.config(text="YAYYAYAAYA GOOD JOBBBBB")
            answers.remove(guess)
        else: 
            Checked.config(text="grrrr NOOOOOO")
    else:
        Checked.config(text="CONGRATS YOU GOT THEM ALLLLLLL")
        newFamily()

Family = ["Rosaceae", "Rutaceae", "Myrtaceae", "Moraceae", "Anacardiaceae", "Euphorbiaceae", "Arecaceae", "Cucurbitaceae", "Ericaceae", "Fabaceae"]
def newFamily():
    New = random.choice(Family)
    x = getFruity(New)
    global answers
    answers = []
    for i in range(len(x)):
        answers.append(x[i]['name'])

    instruct.config(text= f" Can you name all the fruits in the {New} family? ")

Window = Tk()
Window.geometry("500x500")

Title = Label(master=Window, text=" Family Fruity ")
Title.pack()
Enter = Entry(master=Window)
Enter.pack()

instruct = Label(master=Window, text= "")
instruct.pack()


Checked = Label(master=Window, text= "check")
Checked.pack()

Button1 = Button(master=Window, command= checking, text= "GUESS")
Button1.pack()

newFamily()

Window.mainloop()







""" def divide(a,b):
    try: 
        result = a/b
    except ZeroDivisionError: 
        print("Cannot divide by 0")
    else: 
        print(a/b)



divide(10,0) """