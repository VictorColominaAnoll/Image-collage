class Table():
    
    def __init__(self, number_of_images, logo=None):
        # self.rows = rows
        # self.columns = columns
        self.number_of_images = number_of_images
        self.logo = logo

    def print(self):
        if(self.logo == None):
            return ""
        
        rows_length = self.logo.rows
        columns_length = int((self.logo.columns + self.number_of_images) / self.logo.rows)
        
        logo_columns = self.getColumnsWhereTheLogoShouldBePlaced(columns_length)
        result = ""
 
        for row in range(0, rows_length):
            for col in range(0, columns_length):
                if(col in logo_columns):
                    result = result + "l "
                else:
                    result = result + "x "
            result = result + "\n"

        return result

    def getColumnsWhereTheLogoShouldBePlaced(self, columns_length):
        result = []
        for x in range(0, self.logo.columns):
            result.append(int(columns_length / 2) + x)
        return result
    

