# Creating an abstract class for solution
from abc import ABC, abstractmethod


class SwitchAble(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SwitchAble):
    def turn_on(self):
        print("Light Turning on")

    def turn_off(self):
        print("Light Turning off")


class Switch:

    def __init__(self, appliance):  # Tightly coupled with Light, breaking Dependancy Inversion, So always looks at
        # abstract classes
        self.appliance = appliance

    def toggle(self, state):
        if state == "on":
            self.appliance.turn_on()
        else:
            self.appliance.turn_off()


light = Light()
s = Switch(light)
s.toggle("on")
s.toggle("off")


class Fan(SwitchAble):

    def turn_on(self):  # WE are force to change the name back now
        print("Fan Turning on")

    def turn_off(self):  # WE are force to change the name back now because of Abstract class
        print("Fan Turning off")


# By adding this we can resolve the issue
# But when you go to electrician shop you cannot say give me switch for fan , switch for fan separately
# So this is not correct solution
# the concrete solution is to create an Abstract class
#  SwitchFan:
#
#     def __init__(self, light):
#         self.light = light
#
#     def toggle(self, state):
#         if state == "on":
#             # self.light.turn_on_fan() # WE are force to change the name now
#             self.light.turn_on()
#         else:
#             # self.light.turn_off_fan() # WE are force to change the name now
#             self.light.turn_off()

f = Fan()
s2 = Switch(f)
s2.toggle("on")  # This can go wrong at runtime
s2.toggle("off")


class Microwave(SwitchAble):
    def turn_on(self):
        print("Microwave Turning on")

    def turn_off(self):
        print("Microwave Turning off")


m = Microwave()
s3 = Switch(m)
s3.toggle("on")
s3.toggle("off")
