from PIL import Image
from domain.table import Table
import os
import random

def add_photo(image_name, x, y):
    image = Image.open("./images/" + image_name)
    image = image.resize((x_image_size, y_image_size))

    blank_image.paste(image, (x, y))
    blank_image.save("result.jpg")

def includeLogo(x, y):
    middle = (x,y)
    blank_image.paste(logo, middle, logo)

    blank_image.save("result.jpg")

def getImages():
    list = []
    for filename in os.listdir("./images"):
        list.append(filename)

    random.shuffle(list)
    return list

images = getImages()

table = Table(len(images))

isLogoIncluded = False

x_image_size = 100
y_image_size = 100

x_logo_size = 250
y_logo_size = 250

white_space_size = 25

blank_image = Image.new(mode = "RGB", size = (table.getTotalImageSize(), table.getTotalImageSize()), color="white")

logo = Image.open("main_logo.png")
logo = logo.resize((x_logo_size, y_logo_size))

x = 50
y = 50

distribution = table.print()

for index in range(0, len(distribution)):
    current_value = distribution[index]

    if(current_value == "x"):
        add_photo(images.pop(), x, y)
    elif(current_value == "l" and not(isLogoIncluded)):
        isLogoIncluded = True
        includeLogo(x, y)
    
    if(current_value == "s"):
        x = 50
        y = y + y_image_size +  white_space_size
    else:
        x = x + x_image_size + white_space_size