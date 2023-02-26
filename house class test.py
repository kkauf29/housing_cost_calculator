###
# Kim Kaufman
# Advanced Python Final
# Tests House class

from House_Class import House

    
def get_square_footage():    
    while True:
        try:
            square_footage = float(input("Please enter the square footage: "))
            return square_footage
        except ValueError:
            print("Please enter numbers only")
            continue
        
def get_number_baths():    
    while True:
        try:
            number_baths = float(input("Please enter the number of baths:"))
            return number_baths 
        except ValueError:
            print("Please enter numbers only")
            continue   
    

def get_number_bedrooms():    
    while True:
        try:
            number_bedrooms = int(input("Please enter the number of bedrooms: "))
            return number_bedrooms
        except ValueError:
            print("Please enter numbers only")
            continue   
          
           
def get_age_house():    
    while True:
        try:           
           age_house = int(input("Please enter the age of the house: "))
           return age_house
        except ValueError:
            print("Please enter numbers only")
            continue   
           
                 
def get_condition():        
    while True:   
        condition = input("Please enter the house condition (new, good, poor): ")
        if condition != "new" or condition != "good" or condition != "poor":
            print("Please only enter either new, good, or poor")
            return condition  
        else:
            break   
       

def main(): 
    square_footage = get_square_footage()
    number_baths = get_number_baths()
    number_bedrooms = get_number_bedrooms()
    age_house = get_age_house()
    condition = get_condition()        
    house1 = House(square_footage, number_baths, number_bedrooms, age_house, condition)
    
    house_cost = house1.house_cost()
    
    print(f"The cost of this house is {house_cost}")     
             
main()                                      