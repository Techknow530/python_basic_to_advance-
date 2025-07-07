class Car:
    # __model = "" #private
    # _color = ""  #protected 
    # typ= ""   #public
    def __init__(self,model_name,color,typ):
        self.__model = model_name
        self._color = color
        self.typ = typ
    def show(self):
        print(f" ------------------------------------\n name : {self.__model} \n color : {self._color} \n type : {self.typ} \n---------------------------")



bmw = Car('m4','red','seddan')
print(bmw._Car__model) # It's to accses private variable in python outside of class 
bmw.show()

