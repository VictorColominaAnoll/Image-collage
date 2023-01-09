from PIL import Image

def add_photo(x, y):
    image = Image.open("1.jpg")
    image = image.resize((x_image_size, y_image_size))

    blank_image.paste(image, (x, y))
    blank_image.save("result.jpg")

def includeLogo(x, y):
    middle = (x,y)
    blank_image.paste(logo, middle, logo)

    blank_image.save("result.jpg")


# print("Insert logo size:")
# main_logo_size = int(input())
main_logo_size = int(input())

print("Insert rows:")
# max_row = int(input())
max_row = 4

print("Insert cols:")
# max_col = int(input())
max_col = 5

number_of_photos = 15
total_number = number_of_photos + main_logo_size

isLogoIncluded = False

x_image_size = 100
y_image_size = 100

x_logo_size = 100
y_logo_size = 200

white_space_size = 25

blank_image = Image.new(mode = "RGB", size = (1920, 1080), color="white")

logo = Image.open("main_logo.png")
logo = logo.resize((x_logo_size, y_logo_size))


y = 150

for row in range(1, max_row):
    x = 100
    for col in range(1, max_col):
        if ((row == 3 or row == 4) and col == 5):
            if(isLogoIncluded == False):
                isLogoIncluded = True
                includeLogo(x, y)
        else:
            add_photo(x, y)
        x = x + x_image_size + white_space_size
    y = y + y_image_size +  white_space_size


# for pic in range(1, number_of_photos + main_logo_size):

# add_photo(100, 100)
# add_photo(100, 300)
# add_photo(100, 500)

# add_photo(300, 100)
# add_photo(300, 300)
# add_photo(300, 500)

# add_photo(500, 500)
# add_photo(700, 500)
# add_photo(1100, 500)
# add_photo(1300, 500)
# add_photo(1500, 500)
# add_photo(1700, 500)