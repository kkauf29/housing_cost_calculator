###
# Kim Kaufman
# Advance Python final
# creates the House Class


class House:
    def __init__(self, square_footage, number_baths, number_bedrooms, age_house, condition):
        self._square_footage = square_footage
        self._number_baths = number_baths
        self._number_bedrooms = number_bedrooms
        self._age_house = age_house
        self._condition = condition
        
    def __repr__(self):
        return f"sqaure footage: {self._square_footage}, number of baths: {self._number_baths}, number of bedrooms: {self._number_bedrooms}, age of house: {self._age_house}, condition: {self._condition}"    
    
    def house_cost(self):
        houseCost = self._square_footage * 150
        
        if self._age_house > 20:
            houseCost = houseCost - (houseCost * .15)
        
        if self._condition == "good":
            houseCost = houseCost - (houseCost * .05)
        
        elif self._condition == "poor":
            houseCost = houseCost - (houseCost * .1)
            
        else:
            houseCost = houseCost
            
        return houseCost            