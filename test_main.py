from PIL import Image
from domain.table import Table
import os
import random

def add_photo(image_name, x, y):
    # image = Image.open("./images/" + image_name)
    image = Image.open(image_name)
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

# images = getImages()

table = Table(89)

isLogoIncluded = False

#variables
x_image_size = 106
y_image_size = 104

x_logo_size = 310
y_logo_size = 232
#end_variables



x_white_space_size = 50
y_white_space_size = 25

blank_image = Image.new(mode = "RGB", size = (1920, 1080), color="white")

## (8 * 100) + (50 * 5) -> 

## images (5 * 100) + white_space (50 * 5) -> 1080

### Whitespace should be a fix value / decided by the user
### The size image should be calculated based on the total size of the image + the total whitespace value

logo = Image.open("main_logo.png")
logo = logo.resize((x_logo_size, y_logo_size))

x = 50
y = 50

# distribution = table.print()
# distribution = "xxxxxxxxxxxxxxsxxxxxxxxxxxxxxsxxxxxxxxxxxxxxsxxxxxxllxxxxxxsxxxxxxllxxxxxxsxxxxxxxxxxxxxxsxxxxxxxxxxxxxxsxxxxxxxxxxxxxxsxxxxxxxxxxxxx"
distribution = "xxxxxxxxxxxxsxxxxxxxxxxxxsxxxxxxxxxxxxsxxxxxllxxxxxsxxxxxllxxxxxsxxxxxxxxxxxxsxxxxxxxxxxxxsxxxxxxx"

for index in range(0, len(distribution)):
    current_value = distribution[index]

    if(current_value == "x"):
        add_photo("1.jpg", x, y)
    elif(current_value == "l" and not(isLogoIncluded)):
        isLogoIncluded = True
        includeLogo(x, y)
    
    if(current_value == "s"):
        x = 50
        y = y + y_image_size +  y_white_space_size
    else:
        x = x + x_image_size + x_white_space_size