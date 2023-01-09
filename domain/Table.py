class Table():
    
    def __init__(self, number_of_images, logo=None):
        # self.rows = rows
        # self.columns = columns
        self.number_of_images = number_of_images
        self.logo = logo

    def print(self):
        if(self.logo == None):
            return ""
        
        rows_length = int((self.logo.columns + self.number_of_images) / self.logo.columns)
        print(rows_length)

        columns_length = self.logo.columns
        
        result = ""

        for row in (0, rows_length):
            for col in (0, columns_length):
                if(int(columns_length / 2) == col):
                    result = result + "l "
                else:
                    result = result + "x "
        
        return result