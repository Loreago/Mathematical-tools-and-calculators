from math import tan,pi
class Polygon:
    greek_unit_prefix={0:"", 1:"hen",2: "di", 3: "tri", 4: "tetra", 5: "penta", 6: "hexa", 7: "hepta", 8: "octa", 9: "ennea"}
    greek_tens_suffixes={10: "conta", 100: "hecta", 1000: "chilia", 10000: "myria", 100000: "kismyria"}
    def __init__(self,number_of_sides: int, side_length: int):
        self.__number_of_sides=number_of_sides
        self.__side_length=side_length
    @property
    def number_of_sides(self):
        return self.__number_of_sides
    @number_of_sides.setter
    def number_of_sides(self,number_of_sides: int):
        self.__number_of_sides=number_of_sides
    @property
    def side_length(self):
        return self.__side_length
    @side_length.setter
    def side_length(self,side_length: int):
        self.__side_length=side_length
    def area(self):
        return self.area_of_polygon(self.number_of_sides,self.side_length)
    @classmethod
    def area_of_polygon(cls,number_of_sides: int, side_length: int):
        return number_of_sides*((side_length**2)/(4*tan(pi/number_of_sides)))
    def perimeter(self):
        return self.number_of_sides*self.side_length
    def interior_angle(self):
        return ((self.number_of_sides-2)*180)/self.number_of_sides
    def sum_of_interior_angles(self):
        return ((self.number_of_sides-2)*180)
    def exterior_angle(self):
        return 360/self.number_of_sides
    def no_of_diagonals(self):
        return ((self.number_of_sides*(self.number_of_sides-3))//2)
    def __name_of_polygon(self):
        polygon_name=""
        if self.number_of_sides<10:
            polygon_name=self.greek_unit_prefix[self.number_of_sides]+"gon"
        elif 10<=self.number_of_sides<20:
            number_string=str(self.number_of_sides)
            prefix=self.greek_unit_prefix[int(number_string[1])]
            if number_string[1]=="2" and 10<self.number_of_sides<20:
                prefix="do"
            polygon_name=prefix+"decagon"
        return polygon_name
    def __str__(self):
        if self.__name_of_polygon()!="":
            return f"regular {self.__name_of_polygon()} with a side length of {self.side_length}"
        else:
            return f"regular {self.number_of_sides}-gon with a side length of {self.side_length}"
    
if __name__=="__main__":
    my_polygon=Polygon(23,10)
    print(my_polygon)
    print(my_polygon.area())
    print(my_polygon.perimeter())
    print(my_polygon.no_of_diagonals())
    print(Polygon.area_of_polygon(50,10))