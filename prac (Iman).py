##EXCEPTION HANDLING
##using try block
try:
    numerator = int(input("enter a number: "))
    denomenator = int(input("enter a number: "))

    result = numerator / denomenator
    
#using except block1
except ZeroDivisionError:
    print(f"Division by zero is not allowed")

#using except block2
except ValueError:
    print(f"Invalid input. Please enter numeric values")

#if try block has no error than execute else block
else:
    print(result)

#finally will execute if there's any exception
finally:
    print("Program executed successfully")


##LAMBDA FUNCTION

x = lambda a, b : a[0] == b
print(x("ball", "b"))


##CLASSES AND OBJECTS

##define a class
class SmartDevice:
    #define attributes 
    def __init__ (self, name, device_type, device_status = "OFF"):
        self.name = name 
        self.device_type = device_type 
        self.device_status = device_status

    #define function
    def turn_on(self):
        if self.device_status == "ON":
            print(f"{self.name}, {self.device_type}, {self.device_status} is ON")

        else:
            print(f"{self.name}, {self.device_type}, {self.device_status}, is OFF")

#creating objects
device1 = SmartDevice("LED light", "light", "ON")
device2 = SmartDevice("Audionic speaker", "speaker", "Off")
device3 = SmartDevice("Royal Fan", "fan", "ON")

#calling functions
device1.turn_on()
device2.turn_on()
device3.turn_on()