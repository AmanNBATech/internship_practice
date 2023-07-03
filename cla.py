# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     def get_grade(self):
#         return self.grade

#     def set_name(self, new_name):
#         self.name = new_name

#     def set_age(self, new_age):
#         self.age = new_age

#     def set_grade(self, new_grade):
#         self.grade = new_grade


# student1 = Student("John Smith", 17, 11)


# print("Name:", student1.get_name())
# print("Age:", student1.get_age())
# print("Grade:", student1.get_grade())

# student1.set_name("Jane Doe")
# student1.set_age(16)
# student1.set_grade(10)

# print("Updated Name:", student1.get_name())
# print("Updated Age:", student1.get_age())
# print("Updated Grade:", student1.get_grade())




#  simple program of class
class veh:
    def __init__(self,brand,model,price,year):
        self.brand=brand
        self.model=model
        self.price=price
        self.year=year

    def brand_name(self):
        return self.brand
    def model_name(self)    :
        return self.model

    def price_(self):
        return self.price
    def _year(self):
        return self.year
car = veh("Bajaj","pulsar",200000,2009)
print("Brand",car.brand_name())   
print("model",car.model_name())   
print("Price of Car",car.price_())   
print("manufactured year",car._year())   