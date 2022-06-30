import tkinter
import requests
import wget
from tkinter import ttk
from tkinter.constants import Y
from PIL import ImageTk, Image
from random import randint
from time import sleep


window = tkinter.Tk()
window.geometry("500x500")

image1 = Image.open("dog.jpg")
image1 = image1.resize((350, 350), Image.ANTIALIAS)

test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
label1.pack()


def get_dog_pic():

    dog_url = requests.get("https://dog.ceo/api/breeds/image/random")
    dog_url = dog_url.json()
    result = dog_url['message']
    dog_file_name = "dog" + str(randint(0, 999)) + ".jpg"
    response = wget.download(result, dog_file_name)

    global new_image
    new_image = Image.open(dog_file_name)
    new_image = new_image.resize((350, 350), Image.ANTIALIAS)

    new_image = ImageTk.PhotoImage(new_image)


def replace():
    label1.config(image=new_image)


btn1 = ttk.Button(text="Get Random Dog", command=get_dog_pic)
btn1.pack()
btn2 = ttk.Button(text="Replace", command=replace)
btn2.pack()

window.mainloop()
