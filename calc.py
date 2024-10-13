"""convert spring rates"""

class CalcClass:
    def calc_method(self):
       print("I'm an automotive calculator!")

# an instance of calculator
calc_instance = CalcClass()
calc_instance.calc_method()

class UnitConvert:
    kg_in_lb = 2.2

    def __init__(self, kg):
        self.kg = kg

    # class method
    def convert_kg_lb(self):
        """kg_to_lbs ="""
        return self.kg * self.kg_in_lb
        #print(kg_to_lbs)rt

    """def result(self):"""


UnitConvert(10)

"""converter = UnitConvert()
kg_in_3mi = converter.convert_kg_lb(CalcClass.kg)
print(kg_in_3mi)"""


"""calc_instance_type = type(calc_instance)
print(calc_instance_type)"""


print(150**2)