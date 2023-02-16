class Table():
    
    def __init__(self, number_of_images):
        self.logo_size = 4
        self.number_of_images = number_of_images

        self.size_of_the_square_side = self.getSquareSize(number_of_images)

    def getTotalImageSize(self):
        image_size = 100
        whitespace = 25
        margin = 75
        
        return self.size_of_the_square_side * (whitespace + image_size) + margin

    def print(self):
        if(self.number_of_images == 0): 
            return ""

        logo_coordinate = int((self.size_of_the_square_side / 2) - 1)
        return self.getImagesDistribution(logo_coordinate)

    def getImagesDistribution(self, logo_coordinate):
        result = ""
        images_count = 0
 
        for row in range(0, self.size_of_the_square_side):
            for col in range(0, self.size_of_the_square_side):
                if(images_count < self.number_of_images): 
                    if(self.isLogoCoordinate(row, col, logo_coordinate)):
                        result = result + "l"
                    else:
                        result = result + "x"
                        images_count = images_count + 1

            result = result + "s"

        return result

    def isLogoCoordinate(self, row, col, logo_coordinate):
        if(row == logo_coordinate and col == logo_coordinate): return True
        elif(row == logo_coordinate and col == logo_coordinate + 1): return True
        elif(row == logo_coordinate + 1 and col == logo_coordinate): return True
        elif(row == logo_coordinate + 1 and col == logo_coordinate + 1): return True

        return False

    def getSquareSize(self, total_images):
            square_size = 1

            while((square_size * square_size) < (total_images + self.logo_size)):
                square_size = square_size + 1
             
            return square_size
