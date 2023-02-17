class Table():
    
    def __init__(self, number_of_images):
        self.number_of_images = number_of_images
        self.logo_size = 4

        length = 4
        height = 2

        while((length * height) < number_of_images):
            if(height + 1 < length - 2):
                height += 1
            else:
                length += 2

        self.length = length
        self.height = height

    def print(self):
        if(self.number_of_images == 0): 
            return ""
        
        return self.getImagesDistribution()

    def getImagesDistribution(self):
        result = ""
        images_count = 0
        
        for x in range(0, self.height):
            for y in range(0, self.length):
                if(self.isValidToAddImage(images_count)):
                    if(self.isLogoCoordinate(x, y)):
                        result = result + "l"
                    else:
                        result = result + "x"
                        images_count = images_count + 1
            
            if(self.isValidToAddImage(images_count)):
                result = result + "s"

        return result

    def isValidToAddImage(self, images_count):
        return  images_count < (self.number_of_images - self.logo_size)

    def isLogoCoordinate(self, x, y):
        logo_height = int((self.height / 2) - 1)
        logo_length = int((self.length / 2) - 1)

        if(x == logo_height and y == logo_length): return True
        elif(x == logo_height + 1 and y == logo_length): return True
        elif(x == logo_height and y == logo_length + 1): return True
        elif(x == logo_height + 1 and y == logo_length + 1): return True

        return False

    def getImageLength(self):
        white_space = 50

        return round((1920 - ((white_space * self.length) + 50)) / self.length)

    def getImageHeight(self):
        white_space = 25

        return round((1080 - ((white_space * self.height) + 50)) / self.height)

    def getLogoLength(self):
        return (self.getImageLength() * 2) + (50 * 2) - 2

    def getLogoHeight(self):
        return (self.getImageHeight() * 2) + 25 - 1


# def getSquareSize(self, total_images):
#         square_size = 1

#         while((square_size * square_size) < (total_images + self.logo_size)):
#             square_size = square_size + 1
            
#         return square_size

# def getTotalImageSize(self):
#     image_size = 100
#     whitespace = 25
#     margin = 75
    
#     return self.size_of_the_square_side * (whitespace + image_size) + margin