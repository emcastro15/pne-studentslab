class Car:
    def __init__(self, brand):
        self.car_brand = brand
        self.speed = 0
        self.value = 0
        #brand+= "TM"

    def set_speed(self, speed):
        self.speed = speed
        #self.brand += "TM"

    def get_speed(self):    #there is no need for this function
        return self.speed

    def get_brand_nationality(self):
        if self.car_brand == "Renault":
            return "France"
        elif self.car_brand == "Ferrari":
            return "Italy"

    def set_age(self, age):
        self.age = age

    def set_value(self, value):
        self.value = value


mycar = Car("Renault")
print(mycar.get_speed())
mycar.set_speed(80)
print(mycar.get_speed())
print(mycar.speed) #this is much better

print(mycar.get_brand_nationality())

yourcar = Car("Ferrari")
print(yourcar.speed)
print(yourcar.get_speed())

class Vehicle:
    def set_speed(self, speed):
        self.speed =speed


class Car(Vehicle):
    def __init__(self, brand, speed=0):
        self.car_brand = brand
        self.speed = speed


class Ferrari (Car):
    def __init__(self):
        super().__init__("Ferrari", 100)
        self.music = "classic"

    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "Wow"


mycar = Car("Renault")
yourcar = Ferrari("Ferrari")
print(yourcar.car_brand)
print(yourcar.make_cabrio(), "and music is", yourcar.music, "and speed", yourcar.speed)
